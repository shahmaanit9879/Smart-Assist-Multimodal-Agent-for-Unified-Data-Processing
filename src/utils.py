import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_openai_api_key():
    """
    Returns the OpenAI API Key from environment variables.
    Make sure you create a .env file with:
    OPENAI_API_KEY=your_key_here
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "ERROR: OPENAI_API_KEY not found. Create a .env file!"

    return api_key


def save_uploaded_file(uploaded_file, save_path):
    """
    Saves an uploaded file (image/audio) to the given path.
    Used in Streamlit app for image/audio uploads.
    """
    try:
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        return f"Error saving file: {str(e)}"


def format_response(text):
    """
    Basic cleanup for AI responses.
    You can expand this to support markdown, HTML, or rich formatting.
    """
    if not text:
        return "No response generated."

    return text.strip()
