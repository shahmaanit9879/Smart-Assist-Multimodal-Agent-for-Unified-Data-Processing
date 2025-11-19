from agents import CoordinatorAgent
from logger import log_event
from a2a_protocol import A2AProtocol

agent = CoordinatorAgent()
protocol = A2AProtocol()

log_event("System started")

text_output = agent.route("This is an example text")
log_event(f"TextAgent Output: {text_output}")

protocol.send("Coordinator", "TextAgent", "Summarize this text")

image_output = agent.route("example_image.png")
log_event(f"ImageAgent Output: {image_output}")
