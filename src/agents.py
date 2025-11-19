from utils import MathTool
from multimodal import process_image

class TextAgent:
    def __init__(self):
        self.tool = MathTool()

    def process(self, text):
        tool_output = None
        try:
            tool_output = self.tool.run(text)
        except:
            tool_output = None

        return {
            "type": "text",
            "text_summary": text[:100],
            "tool_used": bool(tool_output),
            "tool_output": tool_output
        }

class ImageAgent:
    def process(self, image_path):
        vision = process_image(image_path)
        return {
            "type": "image",
            "image_path": image_path,
            "vision_output": vision
        }

class MultiModalAgent:
    def __init__(self):
        self.text_agent = TextAgent()
        self.image_agent = ImageAgent()

    def process(self, text, image_path):
        t = self.text_agent.process(text)
        i = self.image_agent.process(image_path)

        return {
            "type": "multimodal",
            "text_result": t,
            "image_result": i,
            "final_unified_output": f"Text says: {t['text_summary']} | Image says: {i['vision_output']}"
        }
