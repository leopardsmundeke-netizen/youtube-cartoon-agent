import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent

def load_json(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

def build_episode(topic):
    chars=load_json(Path("config/characters.json"))
    return {
        "topic":topic,
        "format":"animated_cartoon_health_comedy",
        "language":"Pakistani Urdu/Roman Urdu",
        "characters":chars,
        "hook":f"Ali: Doctor sahiba, {topic} ka solution itna mushkil kyun lagta hai?",
        "scenes":[
            {"scene":1,"duration":6,"purpose":"hook","ali":"Doctor sahiba, ek serious problem hai!","doctor":"Pehle problem batao, drama baad mein."},
            {"scene":2,"duration":12,"purpose":"question","ali":f"Mujhe {topic} ke bare mein simple solution chahiye.","doctor":"Chalo simple aur safe basics samajhte hain."},
            {"scene":3,"duration":18,"purpose":"education","ali":"Yani routine important hai?","doctor":"Bilkul. Consistency rakho aur agar masla persistent ya severe ho to qualified doctor se mashwara karo."},
            {"scene":4,"duration":8,"purpose":"takeaway","ali":"Aaj ka lesson: shortcut nahi, smart routine!","doctor":"Exactly. Health tips ko responsibly follow karo."}
        ],
        "safety_notes":["General education only","No diagnosis","No prescription or unsafe dosage","Persistent/severe symptoms: seek professional care"],
        "youtube_metadata":{
            "title":f"{topic} 😂 Doctor Ne Ali Ko Samjha Diya!",
            "description":f"Ali aur Dr. Sara ke saath {topic} ko simple Pakistani Urdu mein samjhein. Educational entertainment only.",
            "hashtags":["#HealthTips","#Urdu","#Cartoon","#Doctor","#Pakistan"]
        }
    }

if __name__=="__main__":
    import os
    topic=os.getenv("EPISODE_TOPIC","Skin care basics")
    print(json.dumps(build_episode(topic),ensure_ascii=False,indent=2))
