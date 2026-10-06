import re

FORBIDDEN = [
    "guaranteed cure", "miracle cure", "100% cure",
    "take this medicine", "double the dose", "triple the dose"
]

def validate_episode(ep):
    errors = []
    required = ["topic", "hook", "scenes", "safety_notes", "youtube_metadata"]
    for key in required:
        if not ep.get(key):
            errors.append(f"missing:{key}")
    if len(ep.get("scenes", [])) < 4:
        errors.append("need_at_least_4_scenes")
    text = str(ep).lower()
    for phrase in FORBIDDEN:
        if phrase in text:
            errors.append(f"unsafe_phrase:{phrase}")
    for i, scene in enumerate(ep.get("scenes", []), 1):
        for key in ["scene", "duration", "purpose", "ali", "doctor"]:
            if key not in scene:
                errors.append(f"scene_{i}_missing:{key}")
    return {"ok": not errors, "errors": errors}

if __name__ == "__main__":
    import json, sys
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    print(json.dumps(validate_episode(data), ensure_ascii=False, indent=2))
