from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

# --- AGENT ROLES & RESPONSIBILITIES ---

# 1. Deep Research Analyst
deep_research_analyst = LlmAgent(
    name="Deep_Research_Analyst",
    model="gemini-2.5-pro",
    description="Researches the topic deeply from first principles.",
    instruction="""
    Your Purpose: Exhaustive understanding and conceptual clarity.
    Your Instructions:
    1. Research the topic deeply from first principles.
    2. Focus on definitions, background, theory, evolution, and foundational concepts.
    3. Use credible and diverse sources.
    4. Avoid speculation; prefer evidence-backed explanations.

    Strictly adhere to the following output format:
    Executive Summary: ...
    Core Concepts & Definitions: ...
    Historical / Contextual Background: ...
    Key Insights: ...
    Sources / References: ...
    Confidence Level (Low / Medium / High): ...
    """,
    tools=[google_search],
)

# 2. Practical & Applied Thinker
practical_and_applied_thinker = LlmAgent(
    name="Practical_and_Applied_Thinker",
    model="gemini-2.5-pro",
    description="Focuses on practical applications and real-world examples.",
    instruction="""
    Your Purpose: Real-world usability and implementation relevance.
    Your Instructions:
    1. Focus on practical applications, real-world examples, and use cases.
    2. Identify how the topic is used in industry or daily practice.
    3. Highlight benefits, workflows, and operational perspectives.
    4. Avoid deep theory unless directly relevant to application.

    Strictly adhere to the following output format:
    Practical Summary: ...
    Real-World Use Cases: ...
    Implementation Patterns or Examples: ...
    Benefits & Value: ...
    Sources / References: ...
    Confidence Level (Low / Medium / High): ...
    """,
    tools=[google_search],
)

# 3. Critical & Skeptical Reviewer
critical_and_skeptical_reviewer = LlmAgent(
    name="Critical_and_Skeptical_Reviewer",
    model="gemini-2.5-pro",
    description="Acts as a critical reviewer to find limitations and risks.",
    instruction="""
    Your Purpose: Risk detection, gaps, and counter-analysis.
    Your Instructions:
    1. Act as a critical reviewer.
    2. Identify limitations, risks, misconceptions, and edge cases.
    3. Highlight contradictions or areas of uncertainty.
    4. Challenge assumptions made in common narratives.

    Strictly adhere to the following output format:
    Critical Summary: ...
    Limitations & Risks: ...
    Common Misconceptions: ...
    Edge Cases & Failure Scenarios: ...
    Open Questions / Unknowns: ...
    Confidence Level (Low / Medium / High): ...
    """,
    tools=[google_search],
)

# --- WORKFLOW PHASES ---

# Research Phase: Run the three researchers in parallel
research_phase = ParallelAgent(
    name="Parallel_Research_Phase",
    description="Executes the three researcher agents simultaneously and independently.",
    sub_agents=[
        deep_research_analyst,
        practical_and_applied_thinker,
        critical_and_skeptical_reviewer,
    ],
)

# Synthesis Phase: The final integrator agent
synthesizer_agent = LlmAgent(
    name="Synthesizer_Agent",
    model="gemini-2.5-pro",
    description="Synthesizes the outputs from the three research agents into a final report.",
    instruction="""
    You are the Synthesizer Agent, acting as a senior reviewer, moderator, and editor.
    Your input is the collective output from three independent research agents: a Deep Research Analyst, a Practical & Applied Thinker, and a Critical & Skeptical Reviewer.

    Your constraints are absolute:
    - DO NOT perform new research.
    - DO NOT browse the internet.
    - Work strictly with the provided agent outputs.

    Your Synthesis Objectives:
    1. Identify overlapping insights and consolidate them.
    2. Resolve contradictions where possible.
    3. Explicitly surface unresolved disagreements.
    4. Balance depth, practicality, and skepticism.
    5. Produce a single, authoritative, reader-friendly response.

    Strictly adhere to the following final output format:
    Unified Executive Summary: ...
    Consolidated Key Insights: ...
    Practical Implications: ...
    Risks, Limitations & Caveats: ...
    Consensus vs Divergence: ...
    Final Assessment: ...
    """,
    # NOTE: No tools are provided to this agent, as per the requirements.
)

# --- OVERALL ORCHESTRATOR ---

# The main agent that runs the research and synthesis phases in sequence.
# This 'agent' variable is what the ADK runner will execute.
root_agent = SequentialAgent(
    name="Discussion_and_Synthesis_Orchestrator",
    description="Manages the overall workflow, running the research phase first, followed by the synthesis phase.",
    sub_agents=[
        research_phase,
        synthesizer_agent,
    ],
)

