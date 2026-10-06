import json
import os
from pathlib import Path

SYSTEM_PROMPT = Path("prompts/system.md").read_text(encoding="utf-8")

def build_episode(topic):
    return {
        "topic": topic,
        "status": "draft",
        "system_prompt": SYSTEM_PROMPT,
        "characters": ["Ali", "Dr. Sara"],
        "next_step": "Connect an LLM provider to generate the final episode JSON."
    }

if __name__ == "__main__":
    topic = os.getenv("EPISODE_TOPIC", "Skin care basics")
    print(json.dumps(build_episode(topic), ensure_ascii=False, indent=2))
