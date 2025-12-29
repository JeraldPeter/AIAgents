# Stock Research Agent - Multi-Stocks Edition

## 📋 Project Overview

The **Stock Research Agent Multi-Stocks Edition** is an advanced AI-powered framework designed to automate and systematize the fundamental analysis of **multiple publicly traded companies simultaneously**. Built on Google's Agent Development Kit (ADK), this project demonstrates the capabilities of multi-agent orchestration to conduct comprehensive financial analysis across three critical dimensions: qualitative assessment, quantitative screening, and valuation analysis.

This framework transforms the methodologies from **Zerodha's Varsity Fundamental Analysis Module** into an intelligent, structured agent-based workflow that provides investors with detailed, citation-backed research reports **for multiple stocks in a single session**.

### Key Difference from Single-Stock Version
✨ **Process multiple stocks (batch mode)** with individual reports for each company, eliminating the need to run analysis repeatedly for different tickers.

### Project Objectives

- **Automate Financial Analysis**: Streamline fundamental analysis for multiple companies in one session
- **Batch Processing**: Process multiple stocks efficiently with clean state management between iterations
- **Ensure Transparency**: Provide fully cited and sourced analysis with complete traceability
- **Maintain Quality Control**: Implement multi-gate approval system to validate business quality before deeper analysis
- **Enable Decision Making**: Deliver executive-level investment recommendations grounded in conservative value investing principles
- **Demonstrate AI Capabilities**: Showcase how multi-agent systems can handle complex, real-world financial tasks at scale

---

## 🏗️ Project Architecture

### Core Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM Model** | Gemini 2.0 Flash | Fast reasoning for financial analysis |
| **Framework** | Google Agent Development Kit (ADK) | Multi-agent orchestration and management |
| **Primary Tool** | Google Search | Real-time data retrieval (news, filings, reports) |
| **Language** | Python 3.x | Implementation language |
| **Data Sources** | Annual Reports, Stock Exchanges (NSE/BSE), Financial Filings | Primary data inputs |

### Agent Architecture Overview

The system implements a **Sequential-Iterative Multi-Agent Architecture** with batch processing for multiple stocks:

```
Input: Multiple Tickers (e.g., "INFY, TCS, WIPRO")
   ↓
[Root Agent] - Master Orchestrator
   ↓
[Stock Extractor Agent] - Parse and extract tickers
   ↓
[Loop Agent] - Iterative Batch Processor
   ├─→ [Batch Manager] - Clear state, set current ticker
   ├─→ [Qualitative Agent] - Business quality assessment (Gate 1)
   ├─→ [Quantitative Agent] - Financial health screening (Gate 2)
   ├─→ [Valuation Agent] - Fair value & price assessment (Gate 3)
   ├─→ [CIO Agent] - Final investment decision synthesis
   ├─→ [Report Agent] - Generate markdown report
   └─→ REPEAT for next ticker
   ↓
Output: Individual reports for each stock
```

### Agent Workflow (Per Stock)

The workflow is designed to be efficient, fail-fast, and handle multiple stocks with clean state:

1. **Stock Extraction**: Parse user input and extract all stock tickers
2. **Iterative Processing Loop**: Process each stock independently with clear state management
3. **Batch Management**: Clear context between iterations to prevent cross-contamination
4. **Per-Stock Analysis**: For each ticker:
   - **Qualitative Analysis**: Checks business quality. If bad, proceed to reporting.
   - **Quantitative Analysis**: Validates financial robustness. If weak, skip valuation.
   - **Valuation Analysis**: Determines intrinsic value and investment recommendation.
   - **CIO Synthesis**: Final investment decision memo.
   - **Reporting**: Generates a downloadable Markdown report.
5. **Loop Control**: Iterate until all stocks are processed
6. **Output**: Individual markdown reports for each analyzed stock

---

## 🤖 Agent Descriptions & Use Cases

### 1. **Root Orchestrator Agent**

**Purpose**: Master controller that manages the complete workflow for multiple stocks.

**Workflow**:
```
PHASE 1: Extraction
   └─ Run Stock Extractor Agent to parse input
   
PHASE 2: Iterative Analysis Loop
   └─ Run Loop Agent for batch processing
   
PHASE 3: Completion
   └─ Aggregate all generated reports
```

---

### 2. **Stock Extractor Agent**

**Purpose**: Parses user input to extract multiple stock tickers cleanly.

**Key Responsibilities**:
- **Ticker Parsing**: Identifies stock symbols from natural language input
- **Cleanup**: Filters out noise words (DO, ANALYSIS, ON, STOCK, etc.)
- **Normalization**: Converts all tickers to uppercase format
- **Storage**: Saves extracted tickers to session state for batch processing

**Input Examples**:
- "Analyze INFY, WIPRO, TCS for investment"
- "Research HDFC Bank, Kotak Mahindra, ICICI Bank stocks"
- "Evaluate RELIANCE & JIOFINANCE for buying"
- "Screen: BAJAJFINSV, HCLTECH, NESTLEIND"

**Output**:
```json
{
  "extracted_stocks": ["INFY", "WIPRO", "TCS"],
  "count": 3,
  "status": "success"
}
```

---

### 3. **Batch Manager Agent**

**Purpose**: Manages the stock processing queue and ensures clean state for each iteration.

**Key Responsibilities**:
- **Queue Management**: Retrieves next ticker from pending stocks list
- **State Clearing**: Clears previous analysis data from session state to prevent context contamination
- **Handoff**: Passes clean ticker context to qualitative agent
- **Loop Control**: Signals termination when all stocks are processed

**State Variables Managed**:
```python
session.state["pending_stocks"]        # List of remaining stocks
session.state["current_ticker"]        # Current stock being analyzed
session.state["completed_reports"]     # Storage for final reports
session.state["qualitative_findings"]  # Cleared each iteration
session.state["quantitative_findings"] # Cleared each iteration
session.state["valuation_findings"]    # Cleared each iteration
session.state["cio_decision"]         # Cleared each iteration
```

**Workflow Logic**:
```
FOR EACH TICKER in pending_stocks:
   ├─ Pop ticker from queue
   ├─ Set current_ticker in state
   ├─ Clear previous analysis findings
   ├─ Return control to qualitative agent
   └─ Loop back for next ticker

WHEN pending_stocks is empty:
   └─ Set escalate = True (terminate loop)
```

**Benefits of Batch Processing**:
- ✅ Processes multiple stocks in one session
- ✅ Prevents context bloat from accumulated analysis
- ✅ Each stock gets a fresh, independent analysis
- ✅ Reduces hallucination risks from context overflow
- ✅ Generates individual reports for each stock
- ✅ Efficient resource utilization

---

### 4. **Qualitative Analyst Agent** (Gate 1: Business Quality Screening)

**Purpose**: The gatekeeper of the analysis pipeline. Assesses the qualitative, non-numeric aspects of a business.

**Key Responsibilities**:
- **Management Integrity Assessment**
  - Analyzes related party transactions for conflicts of interest
  - Evaluates history of dividend payments and capital allocation
  - Assesses management track record and insider shareholding
  - Assesses political dependencies or regulatory vulnerabilities
  
- **Business Moat Analysis**
  - Identifies economic moats (brand, pricing power, switching costs)
  - Assesses business scalability without linear capex growth
  - Evaluates competitive advantages in products, distribution, or costs
  
- **Annual Report Forensics**
  - Compares management claims with actual business performance
  - Analyzes risk disclosures and management commentary on macro trends
  
- **Scuttlebutt & Market Observation**
  - Evaluates product visibility in real-world usage
  - Tracks industry trends affecting the company

**Output**: 
- Management Integrity Score (High/Medium/Low)
- Governance Score (High/Medium/Low)
- Moat Strength Assessment (Wide/Narrow/None)
- Red Flags (if any)
- Verdict: **GO** (proceed to next gate) or **NO-GO** (stop analysis immediately)

**Gate Decision Logic**:
- ❌ **NO-GO Triggers**: Fraud, insider dealing, severe governance issues, ethical concerns
- ✅ **GO Triggers**: Sound management, clear moat, acceptable governance standards

---

### 5. **Quantitative Analyst Agent** (Gate 2: Financial Health Screening)

**Purpose**: Validates financial robustness through 10-point checklist. Ensures the company has the financial strength to sustain its moat.

**10-Point Checklist Analysis**:

1. **Gross Profit Margin (GPM)** - Is it > 20%? Indicates moat strength
2. **Growth Alignment** - Is Revenue growth consistent with Profit growth?
3. **EPS Growth** - Is EPS growing without equity dilution masking bad performance?
4. **Debt Levels** - Debt-to-Equity < 1 preferred; Interest Coverage healthy?
5. **Inventory Management** - Calculate Inventory Turnover & Days. Red flag if building inventory while sales slow
6. **Receivables Quality** - Calculate DSO (Days Sales Outstanding). Is company pushing credit sales?
7. **Cash Flow Quality** - Is Operating CF positive? Compare CFO vs PAT (critical red flag if PAT+ but CFO-)
8. **Return on Equity** - Is ROE > 18-20%?
9. **Complexity** - Does company have too many subsidiaries creating opacity?
10. **Working Capital Health** - Is working capital turnover sustainable?

**Additional Analyses**:
- **5-Year CAGR Calculation**: Revenue and Profit growth trends
- **DuPont Analysis**: Decompose ROE into Net Profit Margin × Asset Turnover × Financial Leverage
- **Cash Flow Trend Analysis**: 5-year operating cash flow pattern
- **Balance Sheet Verification**: Accounting equation integrity

**Output**:
- 10-Point Checklist Score: X/10 (with detailed breakdown)
- CAGR: Revenue and Profit (5-year)
- DuPont Breakdown: (Efficiency %, Activity ratio, Leverage multiplier)
- Cash Flow Verdict: Healthy / Stressed / Manipulated
- Verdict: **PASS** (proceed to valuation) or **FAIL** (stop analysis)

---

### 6. **Valuation Analyst Agent** (Gate 3: Fair Value & Price Assessment)

**Purpose**: Determines intrinsic value and applies margin of safety. Assumes company passed quality and financial gates.

**Relative Valuation Analysis**:
- **P/E Ratio Comparison**: Current vs 3-year historical average vs industry peers vs Nifty 50
- **P/S Ratio**: Price to Sales (useful for cyclical businesses)
- **P/BV Ratio**: Price to Book (useful for financial institutions)
- **Market Context**: Nifty 50 P/E assessment (Overvalued >22x vs Undervalued <16x)

**DCF (Discounted Cash Flow) Valuation**:

1. **Historical FCF Analysis** (5-year):
   - Operating Cash Flow - Capital Expenditure = Free Cash Flow
   - Trend analysis of FCF generation capacity

2. **2-Stage Growth Model Forecast**:
   - **Stage 1 (Years 1-5)**: Conservative growth (max 15-18% for high-growth, lower for stable)
   - **Stage 2 (Years 6-10)**: Tapered growth (typically ~10%)
   
3. **Terminal Value Calculation**:
   - Terminal Growth Rate: Conservative 3-4% MAX (should not exceed long-term GDP growth)
   - Gordon Growth Model: Terminal FCF ÷ (WACC - Terminal Growth Rate)

4. **Discount Rate (WACC) Calculation**:
   - Risk-Free Rate (10-year Government Security yield)
   - Beta (systematic risk relative to market)
   - Cost of Equity (using CAPM)
   - Cost of Debt (interest rate on borrowings)
   - WACC = (E/V × Cost of Equity) + (D/V × Cost of Debt × (1 - Tax Rate))

5. **Intrinsic Value Calculation**:
   - NPV of Stage 1 FCF (Years 1-5)
   - NPV of Terminal Value
   - **Intrinsic Value Per Share = Equity Value ÷ Shares Outstanding**

6. **Margin of Safety Application**:
   - Modeling Error Band: ±10% around intrinsic value
   - Conservative Entry: 30% margin of safety
   - **Buy Price = Lower Band × (1 - 0.30)**

**Output**:
- Relative Valuation Status: Overvalued / Undervalued vs Peers
- DCF Intrinsic Value: ₹X per share
- Intrinsic Value Band: ₹X - ₹Y (±10%)
- Buy Price (with 30% Margin of Safety): ₹Z per share
- Final Recommendation: **STRONG BUY / BUY / HOLD / SELL**

---

### 7. **CIO Agent** (Chief Investment Officer - Final Synthesis)

**Purpose**: Synthesizes all three specialist reports into an executive-level investment decision with clear rationale.

**Decision Hierarchy**:
1. **Evaluate Gate 1 (Qualitative)**: If NO-GO → REJECT entire analysis
2. **Evaluate Gate 2 (Quantitative)**: If FAIL → REJECT entire analysis
3. **Evaluate Gate 3 (Valuation)**: Determine recommendation level (STRONG BUY to SELL)

**Final Investment Summary Components**:
- Executive Summary (2-3 sentences with recommendation)
- Qualitative Pillars (Management, Governance, Moat, Red Flags)
- Financial Health Scorecard (All 10-point metrics)
- Valuation Analysis (DCF, multiples, margin of safety)
- Final Investment Decision & Rationale (3 sentences)
- Risk Warnings & Caveats (Key risks, assumptions to monitor)
- Decision Gates Summary (Visual table of all gate decisions)

**Tone**: Professional, analytical, conservative, capital-preservation focused

---

### 8. **Report Agent**

**Purpose**: Collects all analyses and generates professional markdown reports for each stock.

**Key Responsibilities**:
- **Aggregation**: Gathers full analysis from all specialist agents
- **Formatting**: Preserves rich Markdown formatting (tables, links, bolding)
- **Generation**: Saves compiled analysis as a `.md` file for offline viewing
- **Individual Reports**: Creates separate report for each stock analyzed
- **State Preservation**: Ensures each stock's report is saved independently with correct ticker name

**Output**:
- Professional Markdown files (e.g., `INFY_Investment_Report.md`, `TCS_Investment_Report.md`)
- Complete research trail with citations for each stock
- Ready for sharing, printing, or archival

---

## 📚 Foundational Methodology

This project is built upon the comprehensive fundamental analysis framework from:

**Source**: [Zerodha Varsity - Fundamental Analysis Module](https://zerodha.com/varsity/module/fundamental-analysis/)

The Zerodha Varsity fundamental analysis series provides the theoretical foundation covering:
- Module 1: Introduction to Fundamental Analysis
- Module 2: Understanding the P&L Statement
- Module 3: Understanding the Balance Sheet
- Module 4: Understanding the Cash Flow Statement
- Module 5: Financial Ratios
- Module 6: The DuPont Analysis
- Module 7: Dupont Analysis – The 10-Point Checklist
- Module 8: Valuation – The Basics
- Module 9: Discounted Cash Flow (DCF) Valuation

**Our Implementation**: We have systematized these methodologies into intelligent agent workflows that:
1. **Automate** the research process while maintaining rigor
2. **Standardize** analysis across companies for consistency
3. **Cite** all sources for full transparency and traceability
4. **Gate** the analysis process to ensure quality control
5. **Synthesize** findings into actionable investment decisions
6. **Batch Process** multiple stocks efficiently

---

## 🚀 How to Use the Stock Research Agent (Multi-Stocks)

### Installation & Setup

1. **Clone/Navigate to the repository**:
   ```bash
   cd StockResearchAgent_MultiStocks
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or if using the parent project setup:
   ```bash
   pip install google-adk
   ```

3. **Configure API Keys in .env file**:
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the agent using ADK WEB**:
   ```bash
   adk web
   ```

   This will start an interactive web interface where you can input your stock analysis requests.

### Input Format

**Single Request, Multiple Stocks** - Provide one or multiple stock tickers in a single input:

#### Single Stock:
- "Analyze INFY for investment"
- "Research WIPRO stock"
- "Evaluate HDFC Bank for buying"

#### Multiple Stocks (Batch Processing) - **NEW!**:
- "Analyze INFY, WIPRO, TCS for investment"
- "Research HDFC Bank, Kotak Mahindra, ICICI Bank stocks"
- "Evaluate RELIANCE & JIOFINANCE for buying"
- "Screen these: BAJAJFINSV, HCLTECH, NESTLEIND"

**The system will:**
1. Extract all tickers from your input
2. Process each stock independently through the full 4-gate pipeline
3. Generate individual markdown reports for each stock
4. Clear state between iterations to prevent cross-contamination

### Output Format

For **each stock processed**, the system returns:

1. **Stock Extraction Report**
   - Identified tickers: INFY, WIPRO, TCS
   - Parsed from user input

2. **Qualitative Analysis Report** (Gate 1)
   - Management Integrity Score
   - Governance Score
   - Moat Strength Assessment
   - Red Flags (if any)
   - Verdict: GO or NO-GO
   - Complete citation trail

3. **Quantitative Analysis Report** (Gate 2)
   - 10-Point Checklist Score
   - CAGR Analysis (Revenue & Profit)
   - DuPont Breakdown
   - Cash Flow Verdict
   - Verdict: PASS or FAIL
   - Complete source references

4. **Valuation Analysis Report** (Gate 3)
   - Relative Valuation Status
   - DCF Intrinsic Value
   - Intrinsic Value Band
   - Buy Price (with 30% MOS)
   - Recommendation: STRONG BUY / BUY / HOLD / SELL
   - Complete valuation citations

5. **CIO Investment Memo** (Final Synthesis)
   - Executive Summary
   - Decision Gates Summary
   - Qualitative Pillars
   - Financial Health Scorecard
   - Valuation Analysis
   - Final Recommendation & Rationale
   - Risk Warnings

6. **Downloadable Markdown Reports**
   - Filename: `{TICKER}_Investment_Report.md`
   - One report per analyzed stock
   - Professional formatting with tables and links
   - Complete analysis trail with citations

### Batch Processing Example

**Input:** "Analyze INFY and TCS for investment"

**Execution Flow:**
```
1. Stock Extractor Agent
   └─ Identifies: [INFY, TCS]
   └─ Output: "Found 2 stocks to analyze"

2. Loop Agent - Iteration 1 (INFY)
   ├─ Batch Manager → Set ticker = INFY, clear state
   ├─ Qualitative Agent → Business quality assessment
   ├─ Quantitative Agent → Financial health screening
   ├─ Valuation Agent → Fair value determination
   ├─ CIO Agent → Final investment decision
   └─ Report Agent → Save INFY_Investment_Report.md

3. Loop Agent - Iteration 2 (TCS)
   ├─ Batch Manager → Set ticker = TCS, clear state
   ├─ Qualitative Agent → Business quality assessment
   ├─ Quantitative Agent → Financial health screening
   ├─ Valuation Agent → Fair value determination
   ├─ CIO Agent → Final investment decision
   └─ Report Agent → Save TCS_Investment_Report.md

4. Loop Termination
   └─ All stocks processed, session complete
```

**Output Generated:**
- `INFY_Investment_Report.md` (Complete analysis with citations)
- `TCS_Investment_Report.md` (Complete analysis with citations)
- Full chat conversation showing both analyses
- No context contamination between stocks

### Performance Notes

- **Processing Speed**: Depends on LLM response time and search queries
- **API Calls**: Optimized to minimize redundant searches
- **Memory**: Efficient state management prevents context overflow
- **Scalability**: Can process 10-15 stocks per session before hitting context limits

---

## 🔧 Advanced Configuration

### Model Selection

The system uses **Gemini 2.0 Flash** for fast, efficient reasoning:

```python
# In agent.py
FLASH_MODEL_NAME = "gemini-2.0-flash"

# Alternative options:
# FLASH_MODEL_NAME = "gemini-1.5-pro"  # More capable but slower
# FLASH_MODEL_NAME = "gemini-2.5-pro"  # Experimental
```

### Loop Iterations

Maximum number of stocks to process in a single session:

```python
# In agent.py
max_iterations=15  # Can process up to 15 stocks per session
```

### State Management

The batch processor automatically clears these state variables each iteration:
- `qualitative_findings`
- `quantitative_findings`
- `valuation_findings`
- `cio_decision`
- `last_research_data`

This prevents context contamination and ensures fresh analysis for each stock.

### Stock Batch Processing Configuration

Customize batch behavior in `agent.py`:

```python
def assign_stocks_tool(tool_context, tickerStr: str):
    """
    Configure how stocks are extracted and batched
    """
    tickers = [item.strip() for item in tickerStr.split(",")]
    # Tickers are now ready for batch processing
```

---

## 📊 Citation & Source Tracking

Each agent incorporates **comprehensive citation and source tracking**:

### Qualitative Agent Citations
- Management claims sourced to Annual Report page numbers
- Governance data linked to Corporate Governance reports
- News claims linked to URLs and publication dates
- Red flags traced to regulatory filings or stock exchange announcements

### Quantitative Agent Citations
- All financial metrics sourced to specific financial statements
- Balance sheet items dated (e.g., "As of 31-Mar-2024")
- 5-year trends show all intermediate years with document references
- CAGR calculations show formula with source years
- Red flags explicitly sourced with calculation methodology

### Valuation Agent Citations
- Current stock price: Exchange, time, date (e.g., "NSE Close: ₹X as of 27-Nov-2025 16:00 IST")
- Historical prices: From market data with specific dates
- Growth rate assumptions: Each tied to management guidance, historical performance, or industry data
- Terminal growth rate: Justified against GDP growth with source
- WACC components: Each element individually sourced
- DCF calculation steps: All inputs traceable back to source documents
- Peer selection: Rationale explained and sourced

---

## ⚠️ IMPORTANT DISCLAIMER

### This Tool Is For Demonstration & Educational Purposes Only

**CRITICAL NOTICE**: The Stock Research Agent is designed to **DEMONSTRATE AI AGENT CAPABILITIES** in financial analysis. It is **NOT** a substitute for professional financial advice, and **SHOULD NOT** be used as the sole basis for investment decisions.

### Key Limitations & Risks

1. **AI Hallucinations & Errors**
   - Large Language Models (LLMs) are prone to generating plausible-sounding but inaccurate data
   - LLMs may make up financial figures or misinterpret financial statements
   - The model may make calculation errors despite appearing confident

2. **Data Quality & Completeness**
   - Source data may be incomplete, outdated, or incorrect
   - Real-time stock prices may vary from those cited in the report
   - Financial filings may contain errors or revisions not yet reflected

3. **Valuation Assumptions**
   - Growth rate assumptions are inherently uncertain
   - Market conditions, competitive dynamics, and regulatory changes can invalidate assumptions
   - Terminal value estimates can vary dramatically with small changes in discount rate

4. **Market Risk**
   - Past performance does not guarantee future results
   - Even well-analyzed companies can underperform due to execution failures or industry disruptions
   - External shocks (economic recession, pandemic, regulatory changes) can devastate valuations

5. **Insufficient Human Judgment**
   - Automated analysis lacks the nuance and contextual understanding of experienced analysts
   - AI agents cannot replace human judgment, skepticism, and due diligence
   - Market sentiment and behavioral factors are not adequately captured

### What This Tool Is NOT

❌ **NOT** financial advice
❌ **NOT** an investment recommendation
❌ **NOT** a replacement for qualified financial advisors
❌ **NOT** a guarantee of returns or protection from losses
❌ **NOT** suitable for making standalone investment decisions
❌ **NOT** appropriate for risk-averse or first-time investors

### What This Tool IS

✅ **IS** an educational demonstration of AI agent capabilities
✅ **IS** a research aid to supplement human analysis
✅ **IS** a framework for systematizing fundamental analysis
✅ **IS** a tool for generating initial screening criteria
✅ **IS** an example of multi-agent orchestration in finance
✅ **IS** useful for batch screening multiple companies

---

## 📋 MANDATORY STEPS BEFORE USING FOR INVESTMENT DECISIONS

Before acting on ANY recommendation from this system:

1. **Consult a Qualified Financial Advisor**
   - Speak with a Certified Financial Planner (CFP) or registered investment advisor
   - Get personalized advice based on your complete financial situation and risk tolerance
   - Discuss how findings align with your overall investment strategy

2. **Independent Verification**
   - Download original financial documents from company websites or stock exchange (NSE/BSE)
   - Read full annual reports, not just summaries or agent-generated analyses
   - Cross-check all financial figures with official sources

3. **Additional Research**
   - Read industry reports from recognized research firms
   - Follow company news and regulatory filings
   - Understand competitive positioning within the industry

4. **Risk Assessment**
   - Determine your personal risk tolerance and investment horizon
   - Evaluate impact of potential 50%+ loss on your financial security
   - Consider diversification across multiple sectors and market caps

5. **Tax & Legal Consultation**
   - Consult tax professionals on capital gains implications
   - Ensure investment complies with any organizational policies
   - Review regulatory requirements for your jurisdiction

---

## 🔒 User Responsibility & Accountability

**By using this Stock Research Agent, you acknowledge that:**

- You have read and understood this disclaimer in full
- You understand the limitations and risks outlined above
- You take FULL RESPONSIBILITY for all investment decisions
- You will NOT rely solely on this tool for investment choices
- You will consult qualified professionals before investing
- You accept ALL financial losses from decisions informed by this tool
- You understand that LLMs can and do make mistakes
- You will independently verify all analysis and calculations
- You hold developers and operators harmless for any financial losses

---

## 📄 License & Attribution

This project is provided for educational and demonstration purposes.

**Attribution**: Built on methodologies from Zerodha Varsity Fundamental Analysis Module

**License**: Apache 2.0

---

## 🙏 Final Word

This Stock Research Agent represents the frontier of AI in financial analysis. While powerful, it is a **tool**, not a replacement for human judgment. The most successful investors combine quantitative rigor with qualitative insight, market experience, and disciplined risk management.

**For the multi-stocks edition**: You can now screen multiple companies in a single session, but remember that each requires the same due diligence and verification as a single-stock analysis.

---

## 📞 Support & Feedback

For issues, questions, or feedback about this project, please refer to the main ADK samples repository documentation.

---

**Last Updated**: December 2025
**Version**: Multi-Stocks Edition 1.0
