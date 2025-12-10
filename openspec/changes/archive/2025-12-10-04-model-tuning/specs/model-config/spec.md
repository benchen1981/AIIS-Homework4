# Model Configuration Specifications

## ADDED Requirements

### Requirement: Model Selection

The application MUST use the `gemini-flash-latest` model alias to ensure optimal stability and quota compliance.

#### Scenario: Runtime Configuration
- When the `GeminiService` initializes
- It sets the `model_id` to `gemini-flash-latest`
