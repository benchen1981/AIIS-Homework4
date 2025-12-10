# Proposal: Improve API Stability and Configuration

## Summary
Enhance the application's resilience by fixing configuration errors, implementing retry logic for API calls, and selecting a stable model version.

## Why
The application was failing due to an invalid API key and instability in the `gemini-2.5-flash` model (503 Service Unavailable). Users experienced crashes and inability to communicate with the chatbot.

## What Changes
1.  **Configuration Fix**: Corrected the typo in the `.env` file for `GOOGLE_API_KEY`.
2.  **Robustness**: Implemented exponential backoff retry logic using the `tenacity` library in `services.py`.
3.  **Model Selection**: Switched the default model to `gemini-2.0-flash` to query available/stable models.
