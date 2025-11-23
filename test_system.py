# test_system.py

def test_text_agent():
    assert text_agent.process("Hello") != ""

def test_image_agent():
    assert image_agent.process("sample.jpg") is not None