# main.py
from src.text_agent import handle_text
from src.image_agent import handle_image
from src.audio_agent import handle_audio

def demo():
    print("Smart Assist Demo (simple)")
    t = handle_text("Hello Smart Assist")
    print("Text result:", t)
    i = handle_image(None)  # placeholder
    print("Image result:", i)
    a = handle_audio(None)  # placeholder
    print("Audio result:", a)

if __name__ == "__main__":
    demo()
