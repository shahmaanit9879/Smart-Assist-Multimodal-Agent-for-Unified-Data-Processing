import re

class Guardrails:
    @staticmethod
    def clean_text(text):
        # Remove phone numbers (10 digits)
        text = re.sub(r'\b\d{10}\b', '[HIDDEN]', text)

        # Remove email addresses
        text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[HIDDEN_EMAIL]', text)

        return text
