# safe helper
def safe_process(agent, input_data):
    if not input_data:
        return {"skipped": True, "reason": "input missing", "result": None}
    try:
        out = agent.process(input_data)
        return {"skipped": False, "result": out, "reason": None}
    except Exception as e:
        return {"skipped": True, "reason": str(e), "result": None}