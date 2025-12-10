# Project Context

## Purpose

This project is a "University Major Counseling Chatbot" (大學入學選系諮商師 ChatGPT) designed to help high school students select university majors. It demonstrates how to build a ChatGPT-like application using Google's Gemini API (`google-genai`) and the Gemini-2.5-flash model. It includes both a command-line interface and a web-based user interface using Gradio.

## Tech Stack

- **Languages**: Python 3
- **AI/LLM**: Google GenAI SDK (`google-genai`), Google Gemini Model (`gemini-2.5-flash`)
- **Web Framework**: Gradio
- **Environment**: Jupyter Notebook / Google Colab

## Project Conventions

### Code Style

- Follow standard Python (PEP 8) coding conventions.
- Use clear variable names and comments, especially for educational purposes.
- Keep the notebook structure logical (Imports -> Config -> Core Logic -> UI).

### Architecture Patterns

- **Chat Session Management**: Use `client.chats.create` with history for multi-turn conversations.
- **UI Logic**: Separate the chat logic (`pipi` function) from the UI definition (`gr.Blocks`).
- **State Management**: Use `gr.State` to maintain the chat session across Gradio interactions.

### Testing Strategy

- Manual testing via the command-line interface ("cli_chat_loop").
- Interactive testing via the Gradio web interface.

### Git Workflow

- Commit changes to the notebook and relevant script files.
- **CRITICAL**: Do NOT commit real API keys. Use environment variables.

## Domain Context

- The chatbot acts as a professional counselor for university major selection.
- It should conduct empathetic, informative, and interactive conversations to understand the user's interests and provide suggestions.

## Important Constraints

- **Security**: API Keys must be managed securely (e.g., environment variables, `getpass`). Never hardcode keys in shared code.
- **Quota**: Be mindful of API usage quotas for the Gemini API.

## External Dependencies

- **Google GenAI API**: Requires a valid API Key from Google AI Studio.
- **Gradio**: For the web interface.
