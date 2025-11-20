# src/image_agent.py
from src.guardrails import check_file_size_bytes

def handle_image(file_obj):
    # file_obj expected to be an object that has 'size' attribute when uploaded; as placeholder we accept None
    try:
        size = getattr(file_obj, "size", 0)
    except Exception:
        size = 0
    ok, err = check_file_size_bytes(size)
    if not ok:
        return {"ok": False, "error": err}
    # Placeholder result
    return {"ok": True, "result": "Image processed successfully"}
