
# Future Concept Design System - CSS Injection

def get_custom_css() -> str:
    return """
    <style>
        /* Import futuristic fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=JetBrains+Mono:wght@400;700&display=swap');

        :root {
            --bg-color: #050510;
            --glass-bg: rgba(20, 30, 50, 0.4);
            --glass-border: rgba(100, 200, 255, 0.1);
            --accent-cyan: #00f3ff;
            --accent-blue: #0066ff;
            --text-primary: #e0e0e0;
            --text-secondary: #a0a0b0;
            --glow: 0 0 10px rgba(0, 243, 255, 0.2);
        }

        /* Global Reset & Body */
        .stApp {
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 102, 255, 0.1) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(0, 243, 255, 0.05) 0%, transparent 40%);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
        }

        /* Hide standard Streamlit header/footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Typography */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #fff 0%, var(--text-secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Glassmorphism Containers */
        .glass-container {
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .glass-container:hover {
            border-color: rgba(100, 200, 255, 0.3);
            box-shadow: var(--glow);
        }

        /* Chat Messages */
        .stChatMessage {
            background-color: transparent !important;
            border: none !important;
        }

        .stChatMessage[data-testid="stChatMessageUser"] {
            background: rgba(0, 102, 255, 0.1) !important;
            border: 1px solid rgba(0, 102, 255, 0.2) !important;
            border-radius: 12px 12px 0 12px !important;
            backdrop-filter: blur(8px);
        }

        .stChatMessage[data-testid="stChatMessageAssistant"] {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 12px 12px 12px 0 !important;
            backdrop-filter: blur(8px);
        }

        /* Avatar Styling */
        .stChatMessage .stAvatar {
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
            border-radius: 50%;
            box-shadow: var(--glow);
        }

        /* Input Field Styling */
        .stTextInput input {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid var(--glass-border) !important;
            color: var(--accent-cyan) !important;
            font-family: 'JetBrains Mono', monospace !important;
            border-radius: 8px !important;
            transition: all 0.3s ease;
        }

        .stTextInput input:focus {
            background: rgba(255, 255, 255, 0.05) !important;
            border-color: var(--accent-cyan) !important;
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.1) !important;
        }

        /* Custom Cursor Animation */
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        
        .cursor {
            display: inline-block;
            width: 8px;
            height: 18px;
            background: var(--accent-cyan);
            margin-left: 2px;
            animation: blink 1s infinite;
            box-shadow: 0 0 8px var(--accent-cyan);
        }

        /* Skeleton Loading */
        @keyframes pulse-glow {
            0% { opacity: 0.3; }
            50% { opacity: 0.8; }
            100% { opacity: 0.3; }
        }

        .micro-skeleton {
            display: flex;
            gap: 4px;
            align-items: center;
            height: 20px;
        }

        .skeleton-block {
            width: 8px;
            height: 8px;
            background: var(--accent-cyan);
            border-radius: 2px;
            animation: pulse-glow 1.5s infinite ease-in-out;
        }
        
        .skeleton-block:nth-child(2) { animation-delay: 0.2s; }
        .skeleton-block:nth-child(3) { animation-delay: 0.4s; }

    </style>
    """

def get_skeleton_html() -> str:
    return """
    <div class="micro-skeleton">
        <div class="skeleton-block"></div>
        <div class="skeleton-block"></div>
        <div class="skeleton-block"></div>
    </div>
    """
