import requests
import subprocess
import time

server_url = "https://tools.cognitechs.org/urlopner"
last_url = ""

def open_url(url):
    try:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url])
        print(f"Opened: {url}")
    except Exception as e:
        print(f"Failed to open URL: {e}")

while True:
    try:
        response = requests.get(server_url, timeout=10)
        current_url = response.text.strip()
        if current_url and current_url != last_url:
            last_url = current_url
            open_url(current_url)
        else:
            print("No new URL found.")
    except Exception as e:
        print(f"Error checking URL: {e}")
    time.sleep(5)
