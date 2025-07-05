import os, json
from datetime import datetime
import requests

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# Initialize counter.json if missing
if not os.path.exists("counter.json"):
    with open("counter.json", "w") as f:
        json.dump({"value": 120}, f)

# Load current value
with open("counter.json", "r") as f:
    data = json.load(f)
count = data.get("value", 120)

# Send Discord message
payload = { "content": f"⏳ Only **{count}** days left until you turn 30!" }
requests.post(WEBHOOK, json=payload)

# Decrement and save
data["value"] = max(count - 1, 0)
with open("counter.json", "w") as f:
    json.dump(data, f)
