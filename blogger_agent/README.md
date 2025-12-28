# Blogger Agent - Custom ADK Implementation

A powerful multi-agent system for creating technical blog posts using the Google Agent Development Kit (ADK). This is a customized fork of the ADK samples Blogger Agent, optimized for comprehensive blog post generation with built-in planning, writing, editing, and social media promotion capabilities.

## Features

- **Multi-Agent Architecture**: Orchestrated workflow with specialized sub-agents for different tasks
- **Interactive Workflow**: Collaborate with the agent through a conversational interface
- **Codebase Analysis**: Automatically analyze code repositories to generate contextually relevant content
- **Iterative Editing**: Refine blog posts through multiple feedback cycles
- **Social Media Integration**: Generate social media posts to promote your blog articles
- **Google Gemini Integration**: Leverages Gemini 2.5 Pro and Flash models for high-quality content generation

## Project Structure

```
blogger_agent/
├── agent.py                    # Main orchestrator agent
├── config.py                   # Configuration for models and parameters
├── tools.py                    # Custom tools (save_blog_post_to_file, analyze_codebase)
├── agent_utils.py             # Utility functions for agent operations
├── validation_checkers.py      # Validation logic for content quality
├── sub_agents/                # Specialized sub-agents
│   ├── blog_planner.py       # Generates blog post outlines
│   ├── blog_writer.py        # Writes the blog post content
│   ├── blog_editor.py        # Edits content based on feedback
│   └── social_media_writer.py # Creates social media posts
├── .env                        # Environment variables (API keys)
└── README.md                   # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- Google API Key or Vertex AI credentials
- ADK CLI installed

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd c:\Drive\D\ADK\AIAgents\blogger_agent
   ```

2. **Set up your environment variables:**
   
   Edit the `.env` file and add your Google API key:
   ```
   GOOGLE_API_KEY=<your_google_api_key_here>
   GOOGLE_GENAI_USE_VERTEXAI=false
   ```

   **Alternative: Using Vertex AI credentials:**
   If you prefer to use Vertex AI instead of Google AI Studio, update your config:
   ```
   GOOGLE_GENAI_USE_VERTEXAI=true
   GOOGLE_CLOUD_PROJECT=<your_project_id>
   GOOGLE_CLOUD_LOCATION=global
   ```

3. **Install dependencies (if not using ADK CLI):**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Agent

### Via ADK Web Interface (Recommended)

The agent runs exclusively on the ADK web interface, providing an interactive playground for creating blog posts:

```bash
adk web
```

This will launch a web interface where you can:
- Start a new blog post creation session
- Interact with the agent in a conversational manner
- Upload or reference code directories for analysis
- Receive, review, and refine content iteratively
- Export final blog posts as Markdown files

## Workflow

The `interactive_blogger_agent` guides you through the following steps:

### 1. **Codebase Analysis (Optional)**
If you provide a directory path, the agent analyzes the codebase structure to understand context and generate more relevant content.

### 2. **Planning**
The `robust_blog_planner` sub-agent generates a detailed blog post outline with:
- Title and hook
- Introduction and thesis
- Main body sections
- Conclusion and call-to-action

### 3. **Outline Refinement**
You can provide feedback to refine the outline through multiple iterations until approved.

### 4. **Visual Content Selection**
Choose how to handle images and videos:
- **Upload**: Placeholders for your own images/videos
- **None**: Text-only blog post

### 5. **Content Writing**
The `robust_blog_writer` sub-agent writes the full blog post based on the approved outline, with capabilities to:
- Research relevant information using Google Search
- Include code examples and technical details
- Maintain consistent tone and style

### 6. **Iterative Editing**
The `blog_editor` sub-agent refines the content based on your feedback. This cycle repeats until you're satisfied with the result.

### 7. **Social Media Posts (Optional)**
The `social_media_writer` creates promotional posts for:
- Twitter/X
- LinkedIn
- Facebook
- Other social platforms

### 8. **Export**
Save your finalized blog post as a Markdown file for publishing.

## Configuration

### Models Used

Edit [config.py](config.py) to customize models:

```python
critic_model = "gemini-2.5-pro"      # For evaluation tasks
worker_model = "gemini-2.5-flash"    # For content generation
max_search_iterations = 5             # Maximum research iterations
```

## Custom Tools

### `save_blog_post_to_file(blog_post: str, filename: str)`
Saves the generated blog post to a local file in Markdown format.

**Parameters:**
- `blog_post`: The blog post content
- `filename`: The output filename (e.g., "my_blog_post.md")

### `analyze_codebase(directory: str)`
Analyzes a directory structure to extract codebase context for blog generation.

**Parameters:**
- `directory`: Path to the directory to analyze

**Returns:**
- `codebase_context`: Structured analysis of files and directory structure

## Example Usage

```
User: "I want to write a blog post about building a Python REST API"

Agent: I'll help you create a technical blog post! Let me start by generating an outline for your REST API blog post...

[Generates outline with sections on setup, routing, authentication, etc.]

User: "Can you add a section on error handling?"

Agent: [Refines outline with additional section]

User: "Looks good, write it"

Agent: [Writes full blog post based on outline]

[Agent presents draft and asks for feedback]

User: "Good, but make the examples more concise"

Agent: [Edits and refines content]

User: "Perfect! Save it as 'python_rest_api.md'"

Agent: [Saves file and offers to generate social media posts]
```

## Environment Setup Details

### Using Google AI Studio (Default)

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Create an API key
3. Add to `.env` file:
   ```
   GOOGLE_API_KEY=<your_key>
   GOOGLE_GENAI_USE_VERTEXAI=false
   ```

### Using Vertex AI

1. Set up Google Cloud authentication
2. Uncomment and update the Vertex AI configuration in [config.py](config.py)
3. Set environment variables accordingly

## Customization

### Adding New Sub-Agents

To extend the agent with additional sub-agents:

1. Create a new file in `sub_agents/` directory
2. Define your agent using the ADK `Agent` class
3. Import and use it in [agent.py](agent.py)

### Modifying Agent Behavior

Edit the `instruction` parameter in [agent.py](agent.py) to customize:
- Workflow steps
- Interaction style
- Content guidelines
- Quality standards

## Validation and Quality Checks

The [validation_checkers.py](validation_checkers.py) module provides quality assurance for generated content, ensuring:
- Consistency in formatting
- Compliance with writing standards
- Technical accuracy where applicable

## Troubleshooting

### API Key Issues
- Verify your API key is valid and has the necessary permissions
- Check that `GOOGLE_GENAI_USE_VERTEXAI` is set correctly
- Ensure the key has sufficient quota

### Agent Not Responding
- Check your internet connection
- Verify API credentials are correct
- Check the ADK web interface console for error messages

### File Permission Issues
- Ensure you have write permissions to the output directory
- Verify the filename is valid for your operating system

## Architecture Diagram

```
User Interface (ADK Web)
        ↓
interactive_blogger_agent (Main Orchestrator)
    ├── robust_blog_planner
    ├── robust_blog_writer
    ├── blog_editor
    ├── social_media_writer
    └── Custom Tools
        ├── analyze_codebase
        └── save_blog_post_to_file
```

## Contributing

This is a customized fork of the ADK samples Blogger Agent. For improvements and enhancements:

1. Test changes thoroughly in the ADK web interface
2. Ensure all sub-agents function correctly
3. Validate output quality with various blog topics
4. Document any new features or modifications

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

## Support

For issues and questions:
- Review the ADK documentation
- Check the example usage in this README
- Verify your API configuration
- Consult the [agent.py](agent.py) documentation

## Related Resources

- [Google Agent Development Kit (ADK)](https://adk.ai/)
- [Gemini API Documentation](https://ai.google.dev/gemini-api)
- [Google AI Studio](https://aistudio.google.com/)
