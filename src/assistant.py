from multimodal import process_image_input, process_audio_input

class SmartAssistAI:

    def process_text(self, text):
        """
        Handles normal text input.
        You can later replace this with real AI (OpenAI API).
        """
        return f"Text processed: {text}"

    def process_image(self, image_path):
        """
        Handles image input.
        Calls image processing function from multimodal.py
        """
        result = process_image_input(image_path)
        return f"Image Result: {result}"

    def process_audio(self, audio_path):
        """
        Handles audio input.
        Converts speech → text using multimodal.py
        """
        result = process_audio_input(audio_path)
        return f"Audio Result: {result}"
