# Proposal: Optimize Model Selection for Stability

## Summary
Update the AI model configuration to use `gemini-flash-latest` to resolve persistent quota (429) and availability (503) issues encountered with experimental and specific version tags.

## Why
The application faced significant reliability issues:
- `gemini-2.5-flash`: Returned 503 Overloaded errors.
- `gemini-2.0-flash` / `-exp`: Hit 429 Resource Exhausted quotas rapidly.
- `gemini-1.5-flash`: Was not found (404) for the active API key.

Switching to `gemini-flash-latest` ensures the application uses the most stable, generally available Flash model version suitable for the user's free tier quota.

## What Changes
1.  **Model Configuration**: Updated `services.py` to use `model_id = "gemini-flash-latest"`.
