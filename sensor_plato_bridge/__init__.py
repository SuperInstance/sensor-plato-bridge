"""Maritime sensor data to PLATO tile bridge."""
import time, json, urllib.request
from datetime import datetime

PLATO = "http://localhost:8847"
PLATO_WRITE = f"{PLATO}/submit"

def submit_tile(room, tile):
    tile["domain"] = room
    tile["agent"] = "sensor-bridge"
    data = json.dumps(tile).encode()
    req = urllib.request.Request(PLATO_WRITE, data=data,
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read()).get("status") == "accepted"
    except Exception as e:
        print(f"ERR {room}: {e}")
        return False

def poll_sensors():
    """Poll sensors and submit deltas to PLATO."""
    while True:
        # TODO: real sensor integration
        timestamp = datetime.utcnow().isoformat()
        submit_tile("deck-sensor", {
            "title": f"Sensor reading {timestamp}",
            "body": f"Automated sensor reading at {timestamp}",
            "tags": ["sensor", "automated"],
            "question": "What is the current sensor reading?",
            "answer": f"Reading at {timestamp}"
        })
        time.sleep(300)

def main():
    poll_sensors()
