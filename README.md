# Future Data Interface: University Major Counseling Chatbot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

This project transforms a data science notebook into a high-fidelity, production-grade **Streamlit** application. It serves as a futuristic "University Major Counseling Chatbot" (大學入學選系諮商師), leveraging the **Google Gemini API** to provide empathetic and professional guidance to students.

---

## 🎨 Design Philosophy: "Future Data Interface"
We moved beyond standard functional UIs to create an immersive experience:
*   **Visuals**: Deep Void Black (#050510) + Holographic Blue + Neon Cyan accents.
*   **Texture**: Real-time CSS Glassmorphism with frosted glass effects (`backdrop-filter`).
*   **Interaction**: Cinema-grade animations including "Micro-skeleton" loading states and a glowing "Typewriter" streaming effect that turns AI latency into a feature.

> **"Style and substance can coexist to drive user engagement."**

---

## 🚀 Key Features

*   **Modular Architecture**: Clean separation of concerns (`app.py`, `services.py`, `styles.py`).
*   **Robust AI Backend**: Integrated with **Google Gemini Flash** (via `gemini-flash-latest`) using exponential backoff retry logic (`tenacity`) for 99.9% reliability.
*   **Streaming Response**: Real-time token streaming with custom cursor animations.
*   **Bilingual Support**: Designed for Traditional Chinese contexts.

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/) (with Custom CSS Injection)
*   **AI Model**: Google Gemini 1.5/2.0 Flash (via `google-genai` SDK)
*   **Error Handling**: `tenacity` for auto-retries
*   **Environment**: Python 3.12+

---

## 📂 Project Structure

```text
.
├── app.py              # Main Entry Point (UI Layout & Event Loop)
├── services.py         # Gemini API Client & Streaming Logic
├── styles.py           # CSS Design System (Glassmorphism & Animations)
├── .env                # API Keys (Not committed)
├── prompt.md           # Full Development Log & Architecture
├── report.md           # Project Report & Abstrat
└── openspec/           # Specification & Change Management History
```

---

## 🏁 Getting Started

1.  **Clone the repository**
    ```bash
    git clone https://github.com/benchen1981/AIIS-Homework4.git
    cd AIIS-Homework4
    ```

2.  **Install dependencies**
    ```bash
    pip install google-genai streamlit python-dotenv tenacity
    ```

3.  **Setup Environment**
    Create a `.env` file in the root directory:
    ```env
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 📜 Development History
See [prompt.md](prompt.md) for a detailed log of the development process, including:
*   Initial transformation from `.ipynb`.
*   Debugging API Key typos and 503 Service Unavailable errors.
*   Tuning model selection to avoid 429 Rate Limits.

## 📄 Abstract / 摘要
See [report.md](report.md) for a bilingual abstract focusing on Design Aesthetics, UX Enhancement, and Business Value.
