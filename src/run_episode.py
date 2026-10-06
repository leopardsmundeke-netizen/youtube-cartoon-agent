import json, os
from pathlib import Path
from pipeline import build_episode
from quality import validate_episode
from providers.elevenlabs_adapter import create_voice_plan
from providers.video_adapter import scene_prompt
from providers.youtube_adapter import upload_plan

ROOT = Path(__file__).resolve().parent.parent
topic = os.getenv("EPISODE_TOPIC", "Skin care basics")
episode = build_episode(topic)
check = validate_episode(episode)
episode["quality_check"] = check
episode["voice_plan"] = create_voice_plan(episode["scenes"])
episode["video_plan"] = [
    {"scene": s["scene"], "prompt": scene_prompt(s)} for s in episode["scenes"]
]
episode["upload_plan"] = upload_plan(episode["youtube_metadata"], privacy=os.getenv("YOUTUBE_PRIVACY", "private"))

out = ROOT / "episodes" / "latest-episode.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(episode, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"ok": check["ok"], "output": str(out)}, ensure_ascii=False))
if not check["ok"]:
    raise SystemExit(2)
