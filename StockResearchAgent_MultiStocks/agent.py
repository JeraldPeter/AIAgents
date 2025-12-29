import os
import re
from google.adk.agents import LlmAgent, LoopAgent, SequentialAgent
from google.adk.tools import AgentTool, google_search
# Importing agents defined in the sub-package
from .agents.agent import qualitative_agent, quantitative_agent, valuation_agent, cio_agent, report_agent


# Model configuration
FLASH_MODEL_NAME = "gemini-2.0-flash"

# Tool Definitions
def assign_stocks_tool(tool_context, tickerStr: str):
    """
    Logic to ensure extracted stocks are clean and saved to session state.
    """
    # Store in session state for the loop to access. Split by comma and strip whitespace using a list comprehension
    tickers = [item.strip() for item in tickerStr.split(",")]

    tool_context.session.state["pending_stocks"] = tickers
    # Initialize storage for final reports
    tool_context.session.state["completed_reports"] = [] 
    
    return {"status": "success", "extracted_stocks": tickers}

def stock_batch_manager(tool_context):
    """
    Manages the list of stocks and resets relevant state for specific research agents.
    Directly modifies the session state to clear agent message history.
    """
    state = tool_context.session.state
    pending = state.get("pending_stocks", [])
    
    if not pending:
        # No more stocks to process - signal the LoopAgent to escalate/terminate
        tool_context.actions.escalate = True
        return {"status": "complete", "message": "All stocks processed. Terminating loop."}
    
    # 3. Get the next ticker and update state
    current_ticker = pending.pop(0)
    state["pending_stocks"] = pending
    state["current_ticker"] = current_ticker
    
    return {
        "status": "continue", 
        "ticker": current_ticker,
        "remaining": len(pending),
        "instruction": (
            f"Starting FRESH analysis for {current_ticker}. "
            "Previous message history and findings have been cleared from state."
        )
    }

# Infrastructure Setup for Agents

# 1. Extraction Agent
extractor_agent = LlmAgent(
    name="StockExtractor",
    model=FLASH_MODEL_NAME,
    tools=[google_search],
    output_key="extracted_pending_stocks",
    instruction=(
        "Identify all stock ticker symbols from the user's request by doing the google search and provide only stock symbols in comma separated format. for example, if user request is 'Do analysis on Apple, Microsoft & Google stocks', you should return 'AAPL, MSFT, GOOGL'." 
        "Once you have the list of stock tickers, Move on to next agent to assign them for further analysis."
    )
    
)

#2. Assignment Tool
assignment_agent = LlmAgent(
    name="StockAssigner",
    model=FLASH_MODEL_NAME,
    tools=[assign_stocks_tool],
    instruction=(
        "Once you have the list of stock tickers from the extractor agent. Ideally the values are preset in {extracted_pending_stocks} key, call the `assign_stocks_tool` tool to store them for further analysis."
    )
    
)

# 3. The Iterative Loop (Batch Management -> Research Pipeline -> Reporting)
analysis_loop = LoopAgent(
    name="OrchestratorLoop",
    description="Iterates through stocks, wiping state/messages in each iteration.",
    sub_agents=[
        LlmAgent(
            name="BatchProcessor",
            model=FLASH_MODEL_NAME,
            tools=[stock_batch_manager],
            include_contents='none', # CRITICAL: Wipes context
            instruction=(
                "First, call stock_batch_manager to get the next ticker to analyze. "
                "Once the ticker is assigned from stock_batch_manager and state is fresh, hand off to qualitative_agent,, proceed to next agents for analysis." 
            )
        ),
        qualitative_agent,
        quantitative_agent,
        valuation_agent,
        cio_agent,
        report_agent 
    ],
    max_iterations=15
)

# 4. Root Agent
root_agent = SequentialAgent(
    name="FullInvestmentWorkflow",
    description="Extracts stocks then loops through them with clean context transitions.",
    sub_agents=[
        extractor_agent,
        assignment_agent,
        analysis_loop
    ]
)