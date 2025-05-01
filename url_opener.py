import requests
import subprocess
import time
from datetime import datetime

# Set your server endpoint that returns the latest URL
server_url = "https://tools.cognitechs.org/urlopner/urlopner"
last_url = ""

def log(message):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {message}")

def open_url(url):
    try:
        subprocess.run([
            "am", "start", 
            "-a", "android.intent.action.VIEW", 
            "-d", url,
            "--activity-clear-top",
            "--activity-new-task"
        ])
        log(f"✅ Opened URL: {url}")
    except Exception as e:
        log(f"❌ Failed to open URL: {e}")


log("🚀 Termux URL Opener Started.")
log("📡 Polling server every 5 seconds...")
log(f"🌐 Server URL: {server_url}")
log("⏳ Waiting for new URL to open...")

while True:
    try:
        response = requests.get(server_url, timeout=10)
        current_url = response.text.strip()

        if not current_url:
            log("⚠️ No URL found on server.")
        elif current_url != last_url:
            log(f"🔄 New URL detected: {current_url}")
            last_url = current_url
            open_url(current_url)
        else:
            log("✅ No change in URL.")

    except Exception as e:
        log(f"❌ Error checking URL: {e}")

    time.sleep(5)
