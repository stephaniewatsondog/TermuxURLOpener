import requests
import time
from datetime import datetime

server_url = "https://tools.cognitechs.org/urlopner/urlopner"
last_url = ""
file_path = "/downloads/latest_url.txt"  # Tasker can read this

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

log("🚀 URL Writer Started...")

while True:
    try:
        response = requests.get(server_url, timeout=10)
        current_url = response.text.strip()
        if current_url and current_url != last_url:
            last_url = current_url
            with open(file_path, "w") as f:
                f.write(current_url)
            log(f"📤 New URL written to file: {current_url}")
        else:
            log("✅ No change in URL.")
    except Exception as e:
        log(f"❌ Error: {e}")
    time.sleep(5)
