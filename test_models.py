import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

print("Listing available models:")
try:
    # The SDK method might vary slightly, but standard google.generativeai uses list_models
    # For google-genai SDK 1.x, we check the client methods.
    # Looking at the notebook, it used `client.models.generate_content`.
    # Let's try to list them if possible, or just test a standard one.
    
    # Actually, in the new SDK, it might be client.models.list()
    # But to be safe and quick, let's just inspect the error message advice which said "Call ListModels".
    # I'll try to iterate if the SDK supports it.
    pass 
except Exception as e:
    print(e)
    
# Alternative: just try to generate with gemini-1.5-flash-001
try:
    print("Testing gemini-1.5-flash-001...")
    response = client.models.generate_content(
        model="gemini-1.5-flash-001",
        contents="Hello"
    )
    print("Success with gemini-1.5-flash-001")
except Exception as e:
    print(f"Failed gemini-1.5-flash-001: {e}")

try:
    print("Testing gemini-pro...")
    response = client.models.generate_content(
        model="gemini-pro",
        contents="Hello"
    )
    print("Success with gemini-pro")
except Exception as e:
    print(f"Failed gemini-pro: {e}")
