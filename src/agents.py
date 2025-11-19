class TextAgent:
    def process(self, text):
        return {"type": "text", "summary": text[:100], "length": len(text)}

class ImageAgent:
    def process(self, image_path):
        return {"type": "image", "status": "processed", "path": image_path}

class CoordinatorAgent:
    def __init__(self):
        self.text_agent = TextAgent()
        self.image_agent = ImageAgent()

    def route(self, data):
        if isinstance(data, str):
            return self.text_agent.process(data)
        else:
            return self.image_agent.process(data)
