import os

def voice_available():
    return bool(os.getenv("ELEVENLABS_API_KEY"))

def create_voice_plan(scenes):
    return [{"scene":s["scene"],"voices":{"Ali":"ali_voice_id","Dr. Sara":"doctor_voice_id"}} for s in scenes]
