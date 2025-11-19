class MathTool:
    def run(self, text):
        try:
            result = eval(text)
            return f"Result = {result}"
        except:
            return None
