import os

def youtube_ready():
    return all(os.getenv(k) for k in [
        "YOUTUBE_CLIENT_ID","YOUTUBE_CLIENT_SECRET","YOUTUBE_REFRESH_TOKEN"
    ])

def upload_plan(metadata, privacy="private"):
    return {
        "ready": youtube_ready(),
        "privacy": privacy,
        "title": metadata["title"],
        "description": metadata["description"],
        "hashtags": metadata["hashtags"]
    }
