import requests
import subprocess
import time
from datetime import datetime

server_url = "https://tools.cognitechs.org/urlopner"
last_url = ""

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def open_url(url):
    try:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url])
        log(f"✅ Opened URL: {url}")
    except Exception as e:
        log(f"❌ Failed to open URL: {e}")

log("🚀 URL Listener Started. Polling every 5 seconds...")

while True:
    try:
        response = requests.get(server_url, timeout=10)
        current_url = response.text.strip()
        if current_url and current_url != last_url:
            last_url = current_url
            open_url(current_url)
        else:
            log("No new URL found.")
    except Exception as e:
        log(f"⚠️ Error checking URL: {e}")
    time.sleep(5)
