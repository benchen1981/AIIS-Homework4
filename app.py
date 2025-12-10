import streamlit as st
import time
from services import GeminiService
from styles import get_custom_css, get_skeleton_html
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Future Advisor",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject Global CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "gemini_service" not in st.session_state:
    try:
        st.session_state.gemini_service = GeminiService()
        st.session_state.chat_session = st.session_state.gemini_service.create_chat_session()
        # Add initial welcome message to UI history
        st.session_state.messages.append({
            "role": "assistant",
            "content": st.session_state.gemini_service.description
        })
    except ValueError as e:
        st.error(f"Configuration Error: {e}")
        st.stop()

# Header
st.markdown("""
<div class="glass-container" style="margin-bottom: 2rem; text-align: center;">
    <h1>University Major Counseling</h1>
    <p style="color: var(--accent-cyan); letter-spacing: 2px; font-size: 0.8rem;">FUTURE DATA INTERFACE v2.0</p>
</div>
""", unsafe_allow_html=True)

# Chat History Rendering
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Handler
if prompt := st.chat_input("Enter your query protocols..."):
    # 1. Add user message to state and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Assistant Response Container
    with st.chat_message("assistant"):
        # Placeholder for streaming content
        message_placeholder = st.empty()
        full_response = ""
        
        # A. Micro-skeleton Loading State
        message_placeholder.markdown(get_skeleton_html(), unsafe_allow_html=True)
        # Artificial delay to showing off the skeleton (optional, can be removed for speed)
        time.sleep(0.8) 

        # B. Streaming Response with "Typewriter" effect
        try:
            # We use the generator from service
            response_generator = st.session_state.gemini_service.generate_response_stream(
                st.session_state.chat_session, prompt
            )
            
            first_chunk = True
            for chunk_text in response_generator:
                if first_chunk:
                    # Phase 1: Flash appearance (just start showing)
                    full_response += chunk_text
                    first_chunk = False
                else:
                    # Phase 2: Stream remaining
                    # Simulate token-by-token flow if chunks are too large, 
                    # but usually generator yields small enough chunks.
                    for char in chunk_text:
                        full_response += char
                        # Update placeholder with cursor
                        message_placeholder.markdown(full_response + '<span class="cursor"></span>', unsafe_allow_html=True)
                        time.sleep(0.005) # Subtle Typewriter delay
            
            # Final update without cursor
            message_placeholder.markdown(full_response)
            
            # Save to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            message_placeholder.error(f"System Malfunction: {str(e)}")
