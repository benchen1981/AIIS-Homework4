# Development Log & Project Architecture

## Project Architecture

The project was transformed from a Jupyter Notebook into a professional Python Streamlit application.

### Structure
```
.
├── app.py              # Main Application Entry Point (UI Layout & Interaction)
├── services.py         # Business Logic (Google GenAI Client, Retry Logic, Streaming)
├── styles.py           # Design System (CSS Tokens, Glassmorphism Styling, Animations)
├── .env                # Environment Variables (API Keys)
└── openspec/           # Project Specifications & Change Management
    ├── project.md
    ├── changes/        # History of changes (01-init, 02-streamlit, 03-stability, 04-model)
    └── specs/          # Current System Requirements (chatbot, webapp, api-reliability)
```

## Detailed Prompt History

### 1. Project Initialization
**User**: `openspec init`

**Agent Actions**:
- Initialized OpenSpec directory structure (`.agent/`, `openspec/`).
- Configured "Antigravity" as the AI provider.
- Analyzed `MyChatGPT_with_Google_API_20251210.ipynb` to populate `openspec/project.md` with project context (Python, Gradio, Google GenAI).

**User**: `Update tasks and validate all, then archive the current change to Archive 01-xxx`

**Agent Actions**:
- Created Change `01-project-init`.
- Created initial specs for the chatbot in `specs/chatbot/spec.md`.
- Validated and archived the change to `changes/archive/2025-12-10-01-project-init`.

### 2. Streamlit Upgrade & UI Design
**User**:
```
給我執行計畫
將這個ipynb升級為Python專案，需求如下:
像專業前端程師一樣生成 Streamlit.app
1 具未來感概念語言（要傳達的感覺）
2 玻璃質感半透明背景視覺系統（色票 / 排版 / 玻璃質感）
3 互動與動畫，輸入/回答流程：使用「打字機」流入動畫（token-by-token 模擬）與漸變光標。每次模型回覆，顯示「微骨架」→第一段內容快現 → 其餘內容逐步載入。@[MyChatGPT_with_Google_API_20251210.ipynb]
```

**Agent Actions**:
- Created Change `02-streamlit-upgrade`.
- Proposed a "Future Data Interface" design system with deep void black background (#050510) and neon accents.
- Defined tasks for refactoring code into `app.py`, `services.py`, and `styles.py`.

**User**: `同意執行`

**Agent Actions**:
- Created `.env` template.
- Implemented `services.py`: Extracted Gemini API logic and streaming capability.
- Implemented `styles.py`: Added CSS for glassmorphism, glowing effects, and micro-skeleton animations.
- Implemented `app.py`: Integrated the UI with the design system and streaming logic.

**User**: `Update tasks and validate all, then archive the current change to Archive 01-xxx`

**Agent Actions**:
- Verified all tasks completed.
- Archived the change to `changes/archive/2025-12-10-02-streamlit-upgrade`.

### 3. Execution & Debugging (API Key)
**User**: `execute this project`

**Agent Actions**:
- Installed dependencies (`google-genai`, `dotenv`, `streamlit`).
- Launched the app via `streamlit run app.py`.

**User**:
```
debug
ystem Malfunction: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'API key not valid...}}
```

**Agent Actions**:
- Identified a type in `.env` (Key started with `Iza...` instead of `AIza...`).
- Corrected the API key.

### 4. API Stability & Retry Logic
**User**: `debug System Malfunction: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded...'}}`

**Agent Actions**:
- Updated `services.py` to import `tenacity`.
- Added a `@retry` decorator with exponential backoff to handle 503, 429, and 500 errors.

**User**: `debug System Malfunction: 503 UNAVAILABLE...`

**Agent Actions**:
- Attempted to switch to model `gemini-1.5-flash` (suspected version issue).

### 5. Model Selection Tuning
**User**: `debug System Malfunction: 404 NOT_FOUND...`

**Agent Actions**:
- Checked available models.
- Switched to `gemini-2.0-flash`.

**User**: `debug and change to gemini-2.5-flash System Malfunction: 429 RESOURCE_EXHAUSTED...`

**Agent Actions**:
- Switched back to `gemini-2.5-flash` as requested (but it failed with 503).

**User**: `debug System Malfunction: 503 UNAVAILABLE...`

**Agent Actions**:
- Switched back to `gemini-2.0-flash` (hoping 429 quota cooldown passed).

**User**: `Update tasks and validate all, then archive the current change to Archive 03-xxx`

**Agent Actions**:
- Documented these stability fixes (API key, Retry logic, Model switch) in Change `03-api-stability`.
- Archived as `2025-12-10-03-api-stability`.

### 6. Final Optimization (Quota Management)
**User**: `debug System Malfunction: 429 RESOURCE_EXHAUSTED...`

**Agent Actions**:
- Switched to `gemini-2.0-flash-exp` (experimental tier).

**User**: `debug System Malfunction: 429 RESOURCE_EXHAUSTED...`

**Agent Actions**:
- Switched to **`gemini-flash-latest`**. This alias uses the most stable generally available version, avoiding specific experimental quotas.

**User**: `Update tasks and validate all, then archive the current change to Archive 04-xxx`

**Agent Actions**:
- Documented model tuning in Change `04-model-tuning`.
- Archived as `2025-12-10-04-model-tuning`.

### 7. Documentation
**User**: `除錯過程對話紀錄(prompt)輸出為debug.md`

**Agent Actions**:
- Generated `debug.md` summarizing the specific error codes and resolutions.

**User**: `開發過程對話紀錄(prompt)輸出為prompt.md ，包含專案架構`

**Agent Actions**:
- Generated this `prompt.md` file with full dialogue history.
