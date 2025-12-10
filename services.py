import os
import time
from typing import Generator, List, Dict
from google import genai
from google.genai import types as genai_types
from google.api_core.exceptions import ServiceUnavailable, ResourceExhausted, InternalServerError
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Load environment variables
load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
        self.client = genai.Client(api_key=self.api_key)
        # Switching to the generic 'latest' alias which usually points to the most stable available Flash model
        self.model_id = "gemini-flash-latest"
        
        # System Prompt / Persona
        self.character = (
            "你是一位專門協助高中生選填大學科系的專業諮商師，"
            "能根據學生的興趣、成績、未來職涯方向，提供具體且溫暖的建議。"
            "你的語氣應該是專業、富有同理心且具未來感的。"
        )

        self.description = (
            "你好，我是大學入學選系諮商師。\n"
            "你可以跟我分享你的興趣、擅長的科目、想像中的未來生活，"
            "我會盡力幫你一起思考適合的科系與道路。"
        )

    def create_chat_session(self):
        """Creates a new chat session with initial history."""
        history = [
            genai_types.Content(
                role="model",
                parts=[genai_types.Part(text=self.description)]
            )
        ]
        return self.client.chats.create(
            model=self.model_id,
            config={
                "system_instruction": self.character,
                "temperature": 0.7,
            },
            history=history,
        )

    @retry(
        retry=retry_if_exception_type((ServiceUnavailable, ResourceExhausted, InternalServerError)),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        stop=stop_after_attempt(5),
        reraise=True
    )
    def _send_message_with_retry(self, chat_session, user_input):
        """Helper to send message with retry logic for connection errors."""
        return chat_session.send_message_stream(user_input)

    def generate_response_stream(self, chat_session, user_input: str) -> Generator[str, None, None]:
        """Generates a streaming response from the model with error handling."""
        try:
            response = self._send_message_with_retry(chat_session, user_input)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            # Re-raise to be handled by the UI
            raise e
