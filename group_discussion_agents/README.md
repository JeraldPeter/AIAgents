# Group Discussion Agents - Multi-Perspective Analysis System

A sophisticated multi-agent system that simulates a professional group discussion by running multiple specialized agents in parallel to analyze topics from different perspectives, then synthesizing their findings into a comprehensive report.

## Overview

This project implements a **collaborative intelligence model** where different AI agents with distinct viewpoints and expertise research a topic simultaneously and independently, then synthesize their findings into a balanced, nuanced analysis.

### Key Concept

Instead of a single AI analyzing a topic, this system leverages the **wisdom of multiple perspectives**:
- **Deep Research Analyst** - Provides theoretical depth and foundational knowledge
- **Practical & Applied Thinker** - Focuses on real-world applications and use cases
- **Critical & Skeptical Reviewer** - Identifies risks, limitations, and challenges
- **Synthesizer Agent** - Integrates all perspectives into a cohesive final report

## Use Cases

This system is ideal for:
- **Due Diligence Research** - Technology evaluations, market analysis
- **Decision Making** - Complex topics requiring multiple perspectives
- **Risk Assessment** - Identifying both opportunities and pitfalls
- **Comprehensive Learning** - Understanding topics from theory to practice to criticism
- **Business Intelligence** - Competitive analysis, market research
- **Policy Analysis** - Examining regulations, standards, and best practices
- **Technology Evaluation** - Assessing new tools, frameworks, or methodologies

## Project Structure

```
group_discussion_agents/
├── agent.py           # Main agent definitions and workflow
├── .env              # Environment variables (API keys)
├── __init__.py       # Package initialization
└── README.md         # This file
```

## Architecture

### Agent Roles

#### 1. **Deep Research Analyst** (Depth & Theory)
**Role:** Exhaustive understanding and conceptual clarity

**Focus:**
- Definitions, background, and foundational concepts
- Historical context and evolution of the topic
- Theoretical frameworks and first principles
- Evidence-backed explanations

**Output Format:**
- Executive Summary
- Core Concepts & Definitions
- Historical / Contextual Background
- Key Insights
- Sources / References
- Confidence Level

#### 2. **Practical & Applied Thinker** (Practicality & Implementation)
**Role:** Real-world usability and implementation relevance

**Focus:**
- Practical applications and real-world examples
- Industry use cases and workflows
- Implementation patterns and best practices
- Benefits and operational value

**Output Format:**
- Practical Summary
- Real-World Use Cases
- Implementation Patterns or Examples
- Benefits & Value
- Sources / References
- Confidence Level

#### 3. **Critical & Skeptical Reviewer** (Risks & Limitations)
**Role:** Risk detection, gaps, and counter-analysis

**Focus:**
- Limitations, risks, and misconceptions
- Edge cases and failure scenarios
- Contradictions and assumptions
- Uncertainties and open questions

**Output Format:**
- Critical Summary
- Limitations & Risks
- Common Misconceptions
- Edge Cases & Failure Scenarios
- Open Questions / Unknowns
- Confidence Level

#### 4. **Synthesizer Agent** (Integration & Balance)
**Role:** Senior reviewer who integrates all perspectives

**Focus:**
- Consolidating overlapping insights
- Resolving contradictions
- Surfacing unresolved disagreements
- Balancing depth, practicality, and skepticism
- Producing authoritative, reader-friendly reports

**Output Format:**
- Unified Executive Summary
- Consolidated Key Insights
- Practical Implications
- Risks, Limitations & Caveats
- Consensus vs Divergence
- Final Assessment

## Workflow

```
User Input (Topic/Question)
        ↓
┌─────────────────────────────────────────┐
│     RESEARCH PHASE (Parallel)           │
├─────────────────────────────────────────┤
│  Deep_Research_Analyst                  │
│  ↓                                      │
│  (Uses Google Search)                   │
├─────────────────────────────────────────┤
│  Practical_and_Applied_Thinker          │
│  ↓                                      │
│  (Uses Google Search)                   │
├─────────────────────────────────────────┤
│  Critical_and_Skeptical_Reviewer        │
│  ↓                                      │
│  (Uses Google Search)                   │
└─────────────────────────────────────────┘
        ↓ (Collect Results)
┌─────────────────────────────────────────┐
│     SYNTHESIS PHASE (Sequential)        │
├─────────────────────────────────────────┤
│  Synthesizer_Agent                      │
│  ↓                                      │
│  (NO Tools - Works with collected data) │
│  ↓                                      │
│  Final Comprehensive Report             │
└─────────────────────────────────────────┘
```

## Key Features

### 1. **Parallel Research**
All three research agents work simultaneously to maximize efficiency and independence of thought.

### 2. **Diverse Perspectives**
- Theoretical depth
- Practical applicability
- Critical thinking

### 3. **Structured Output**
Each agent produces output in a consistent, predefined format for easy parsing and synthesis.

### 4. **Comprehensive Synthesis**
The synthesizer consolidates findings while maintaining transparency about agreement/disagreement.

### 5. **Confidence Levels**
Each agent provides a confidence assessment (Low/Medium/High) for its findings.

### 6. **Reference Tracking**
All agents include source citations for traceability.

## Getting Started

### Prerequisites

- Python 3.8+
- Google API Key
- ADK CLI installed

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd c:\Drive\D\ADK\AIAgents\group_discussion_agents
   ```

2. **Set up your environment variables:**
   
   Edit the `.env` file:
   ```
   GOOGLE_API_KEY=<your_google_api_key_here>
   ```

3. **Install dependencies (if needed):**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Agent

### Via ADK Web Interface

```bash
adk web
```

Then select the Group Discussion Agents project and enter your topic or question.

### Via Command Line

```bash
adk run group_discussion_agents
```

Then input your research topic when prompted.

## Example Usage

### Input
```
Topic: What is the impact of artificial intelligence on software development?
```

### Process

**Phase 1: Parallel Research (Runs Simultaneously)**

1. **Deep Research Analyst** researches:
   - Historical evolution of AI in software
   - Foundational ML/AI concepts
   - Academic perspectives
   
2. **Practical & Applied Thinker** researches:
   - Current AI dev tools (GitHub Copilot, ChatGPT, etc.)
   - Industry adoption and use cases
   - Developer workflows
   
3. **Critical & Skeptical Reviewer** researches:
   - Job displacement concerns
   - Code quality and security risks
   - Limitations of AI-assisted coding

**Phase 2: Synthesis**

The synthesizer produces:
- Balanced view of AI's current and potential impact
- Practical implications for developers and companies
- Risks and limitations to consider
- Clear identification of consensus vs. disagreements

### Sample Output Structure

```
UNIFIED EXECUTIVE SUMMARY
- AI is transforming software development across multiple dimensions...

CONSOLIDATED KEY INSIGHTS
- Code generation acceleration: [consensus across all agents]
- Quality concerns: [practical + critical alignment]
- Learning tool potential: [deep research + practical agreement]

PRACTICAL IMPLICATIONS
- Developers should focus on...
- Organizations should consider...

RISKS, LIMITATIONS & CAVEATS
- Code quality verification remains essential
- Security vulnerabilities in AI-generated code
- Job market disruption concerns

CONSENSUS VS DIVERGENCE
- Consensus: AI improves productivity
- Divergence: Long-term impact on junior developer training

FINAL ASSESSMENT
- AI is a transformative tool, but careful integration is essential...
```

## Configuration

### Models Used

All agents use **Gemini 2.5 Pro** by default:
```python
model="gemini-2.5-pro"
```

To change the model, edit [agent.py](agent.py) and modify the `model` parameter in each agent definition.

### Tools Available

- **google_search** - Available to all research agents for web research
- **No tools** - Synthesizer agent intentionally has no tools to prevent new research and ensure synthesis-only operation

### Customization

You can customize agent roles by modifying the `instruction` parameter in each agent definition to change:
- Research focus areas
- Output format
- Depth of analysis
- Tone and style

## Environment Setup

### Getting Your Google API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click "Create API Key"
3. Copy the key
4. Paste into `.env` file:
   ```
   GOOGLE_API_KEY=your_key_here
   ```

## Architecture Design Principles

1. **Independence** - Agents research in parallel without influencing each other
2. **Specialization** - Each agent has a specific mandate and expertise
3. **Structured Output** - Consistent formats enable reliable synthesis
4. **No Tool Pollution** - Synthesizer has no tools to prevent scope creep
5. **Transparency** - Clear identification of agreement and disagreement

## Advanced Topics

### Adding New Agent Perspectives

To add a fourth or fifth perspective agent:

1. Create a new `LlmAgent` with:
   - Unique `name` and `description`
   - Specific `instruction` defining its perspective
   - Reference to `[google_search]` tools
   - Structured output format

2. Add it to the `research_phase` `sub_agents` list

3. Update the `synthesizer_agent` instruction to account for the new perspective

### Modifying Output Formats

Each agent's output format is defined in its `instruction` parameter. Modify these to customize:
- Which sections are included
- The order of sections
- Depth requirements for each section

### Using Different Models

Replace `"gemini-2.5-pro"` with other available models:
- `"gemini-2.5-flash"` (faster, lower cost)
- `"gemini-2.0-pro"` (previous generation)
- Other supported models via ADK

## Troubleshooting

### API Key Issues
- Verify the API key is valid and active
- Check that it has the necessary API enablements
- Ensure the key has sufficient quota

### Agents Not Running
- Verify all agents are listed in `sub_agents` parameters
- Check that `research_phase` and `root_agent` are properly configured
- Review the ADK web interface console for errors

### Poor Quality Synthesis
- Check that all three research agents produced comprehensive outputs
- Verify research agents are using appropriate search terms
- Ensure synthesizer agent instruction is clear

### Slow Execution
- Parallel research phase should run simultaneously; if not, check ADK configuration
- Large research phases may take 2-5 minutes depending on search depth
- Consider using `gemini-2.5-flash` for faster (but less detailed) results

## Performance Considerations

- **Parallel Research Phase**: Runs three agents simultaneously (time = longest single agent)
- **Synthesis Phase**: Sequential (after research completes)
- **Total Time**: Typically 2-5 minutes depending on search depth and internet speed

## Use Case Examples

### Technology Evaluation
```
Topic: Should we migrate from React to Vue.js?

Output Provides:
- Theoretical comparison (Deep Research Analyst)
- Practical migration costs and benefits (Practical Thinker)
- Risks like team retraining and ecosystem concerns (Critical Reviewer)
- Integrated recommendation (Synthesizer)
```

### Market Analysis
```
Topic: What is the current state of the AI coding assistant market?

Output Provides:
- Market history and definitions (Deep Research)
- Existing tools and adoption (Practical)
- Limitations and competitive threats (Critical)
- Actionable market insights (Synthesis)
```

### Risk Assessment
```
Topic: What are the risks of adopting serverless architecture?

Output Provides:
- Foundational concepts of serverless (Deep Research)
- Real-world implementation challenges (Practical)
- Security, vendor lock-in, and scaling issues (Critical)
- Risk mitigation strategies (Synthesis)
```

## License

Copyright 2025 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Key Advantages

- **Holistic Analysis** - Theory + Practice + Critical thinking
- **Better Decision Making** - Multiple perspectives reduce blind spots
- **Risk Awareness** - Critical agent surfaces potential issues
- **Efficiency** - Parallel research saves time vs. sequential analysis
- **Transparency** - Clear identification of consensus vs. disagreement
- **Scalability** - Easy to add more agent perspectives
- **Quality** - Professional-grade analysis for complex topics

## Related Resources

- [Google Agent Development Kit (ADK)](https://adk.ai/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api)
- [Google AI Studio](https://aistudio.google.com/)
- [Group Discussion Methodology](https://en.wikipedia.org/wiki/Focus_group)

## Support

For issues or questions:
- Review the example usage in this README
- Check the [agent.py](agent.py) structure
- Verify API configuration
- Consult the ADK documentation
