import os
import re
from google.adk.agents import LlmAgent, LoopAgent, SequentialAgent
from google.adk.tools import AgentTool, google_search
from .agents.agent import qualitative_agent, quantitative_agent, valuation_agent, cio_agent, report_agent


# In ADK Web, the model is usually inherited from the environment or config.
FLASH_MODEL_NAME = "gemini-2.0-flash"


# Tool Definitions
def extract_stocks_tool(tool_context, user_input: str):
    """
    Logic-based tool to ensure extracted stocks are clean and saved to state.
    """
    tickers = [t.strip().upper() for t in re.split(r'[,\s&]+', user_input) if t.strip()]
    ignored_words = {"DO", "ANALYSIS", "ON", "STOCK", "STOCKS", "AND"}
    tickers = [t for t in tickers if t not in ignored_words]
    
    tool_context.session.state["pending_stocks"] = tickers
     # Initialize a clean storage for final reports to prevent mixing
    tool_context.session.state["completed_reports"] = [] 
    return {"status": "success", "extracted_stocks": tickers}

def stock_batch_manager(tool_context):
    """
    Manages the list of stocks and CLEARS context for the new iteration.
    """
    state = tool_context.session.state
    pending = state.get("pending_stocks", [])
    
    if not pending:
        tool_context.actions.escalate = True
        return {"status": "complete", "message": "All stocks processed. Terminating loop."}
    
     # 1. Clear previous iteration data from the session state to prevent context bloat
    keys_to_clear = [
        "qualitative_findings", 
        "quantitative_findings", 
        "valuation_findings", 
        "cio_decision",
        "last_research_data"
    ]
    for key in keys_to_clear:
        state.pop(key, None)
    
     # 2. Get the next ticker
    current_ticker = pending.pop(0)
    state["pending_stocks"] = pending
    state["current_ticker"] = current_ticker
    
    return {
        "status": "continue", 
        "ticker": current_ticker,
        "remaining": len(pending),
        "instruction": f"Starting FRESH analysis for {current_ticker}. Previous data cleared."
    }

#Infra Setup for Agents
# 1. Extraction Agent (Runs once before the loop)
extractor_agent = LlmAgent(
    name="StockExtractor",
    model=FLASH_MODEL_NAME,
    tools=[extract_stocks_tool],
    instruction=(
        "Identify all stock ticker symbols from the user's request. "
        "Pass the list of identified symbols to the extract_stocks_tool."
    )
)

# 2. Qualitative Research Agent  3# . Quantitative Research Agent  4. Valuation Agent  5. CIO Agent  6. Report Agent
# (Assumed to be defined in agents/agent.py and imported above

# 4. The Iterative Loop (Batch -> qualitative -> quantitative -> valuation -> CIO -> report)
analysis_loop = LoopAgent(
    name="OrchestratorLoop",
    description="Iterates through the list of stocks to perform a full pipeline analysis for each.",
    sub_agents=[
        LlmAgent(
            name="BatchProcessor",
            model=FLASH_MODEL_NAME,
            tools=[stock_batch_manager],
            instruction=(
                "First, call stock_batch_manager to get the next ticker and clear the state."
                "Once the state is cleared and a new ticker is assigned, hand off"
                "to the qualitative_agent to begin the analysis. Do not repeat this step."
            )
        ),
        qualitative_agent,
        quantitative_agent,
        valuation_agent,
        cio_agent,
        report_agent # This will print the summary for the specific stock in each loop iteration
    ],
    max_iterations=15
)

# 5. Root Agent
root_agent = SequentialAgent(
    name="FullInvestmentWorkflow",
    description="Extracts stocks then loops through them for separate research and summary reporting.",
    sub_agents=[
        extractor_agent,
        analysis_loop
    ]
)