# ADK Research Agent - Simplified Version

A simplified fork of the [ADK (Agent Development Kit) Starter Pack](https://github.com/google/adk-samples) designed for quick and easy execution using the ADK Web UI.

## Overview

This project provides a streamlined setup for running ADK agents without the complexity of managing a separate React frontend and FastAPI backend. It leverages the built-in **ADK Web UI** for a complete agent research experience with minimal configuration.

> **Note:** This is a simplified version focused on the core agent functionality. For a full-featured production setup with custom React frontend, see the original [deep-search agent](https://github.com/google/adk-samples/tree/main/python/agents/deep-search).

## Features

✨ **Simple Setup** - Get started in under 2 minutes  
🚀 **ADK Web UI** - Built-in web interface, no frontend development needed  
🧠 **Research Agents** - Pre-configured agents for research, analysis, and reporting  
⚡ **Quick Execution** - Run with a single command

## Prerequisites

- **Python 3.10+** - [Download here](https://www.python.org/downloads/)
- **Google AI Studio API Key** - Get one at [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

> Optional: [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) if using Vertex AI instead of AI Studio

## Quick Start

### 1. Set Environment Variables

Create a `.env` file in the project root with your API key:

```bash
GOOGLE_API_KEY=YOUR_AI_STUDIO_API_KEY
```

**Alternatively, for Vertex AI:**
```bash
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
GOOGLE_CLOUD_LOCATION=us-central1
```

### 2. Run the Agent

```bash
adk web
```

The ADK Web UI will open at `http://localhost:8000` (or the next available port).

## Configuration

Edit agent behavior by modifying the relevant `config.py` or `agent.py` files in your chosen agent directory. Common settings include:

- **Model Selection** - Change the Gemini model used
- **Research Parameters** - Adjust iteration limits, temperature, etc.
- **Tool Configuration** - Enable/disable specific agent tools

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `GOOGLE_API_KEY not found` | Ensure `.env` file exists in project root with your API key |
| `adk web` command not found | Run `pip install google-adk` to install the ADK package |
| Port already in use | ADK will automatically try the next available port |
| Authentication errors | Verify your API key is valid at [aistudio.google.com](https://aistudio.google.com) |

## Resources

- 📚 [ADK Documentation](https://google.github.io/adk-docs/)
- 🔗 [Original ADK Samples Repository](https://github.com/google/adk-samples)
- 💡 [Gemini API Documentation](https://ai.google.dev/docs)
- 🛠️ [Agent Starter Pack](https://github.com/google/agent-starter-pack)

## Next Steps

After running `adk web`, you can:

1. **Interact with the agent** - Use the web UI to submit research queries
2. **Customize agents** - Modify prompts and logic in `agent.py`
3. **Extend tools** - Add new capabilities by defining additional tool functions
4. **Deploy** - For production deployment, consider using the full [Agent Starter Pack](https://googlecloudplatform.github.io/agent-starter-pack/guide/deploy-ui.html)

## License

This project is based on the [ADK Samples](https://github.com/google/adk-samples) from Google Cloud Platform.

---

**Happy researching!** 🚀
