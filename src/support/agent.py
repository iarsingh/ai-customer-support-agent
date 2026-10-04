TOOLS = ["classify", "template"]
WRITES = ("refund", "credit", "charge",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    text = (payload.get("message") or goal).lower(); result = "reset_link" if "login" in text else "status_page" if "down" in text else "human"
    return {"refused": False, "tools": TOOLS, "reply": result, "wrote": False, "applied": False}
