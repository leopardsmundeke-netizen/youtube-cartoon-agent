import os

def video_provider_ready():
    return bool(os.getenv("VIDEO_PROVIDER_API_KEY"))

def scene_prompt(scene):
    return (
        "2D animated Pakistani cartoon, consistent Ali and Dr. Sara characters, "
        "clean colorful clinic environment, expressive faces, cinematic camera, "
        "family-friendly comedy, no text distortion. "
        f"Scene purpose: {scene['purpose']}. Dialogue context: "
        f"{scene['ali']} | {scene['doctor']}"
    )
