def safe_run(agent, input_data):
    if input_data is None:
        return "Input missing — skipping this modality."
    try:
        return agent.process(input_data)
    except:
        return "Error in modality processing."
def confidence_level(score):
    if score > 0.85:
        return "High confidence"
    elif score > 0.60:
        return "Medium confidence"
    else:
        return "Low confidence"