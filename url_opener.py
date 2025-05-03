
import requests
import time
from datetime import datetime

# Device number should be stored in this file manually or during setup
DEVICE_ID_FILE = "/sdcard/device_number.txt"
URL_ENDPOINT = "https://tools.cognitechs.org/urlopner/get_url/{}"
URL_FILE = "/sdcard/latest_url.txt"

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

def get_device_number():
    try:
        with open(DEVICE_ID_FILE, "r") as f:
            return int(f.read().strip())
    except:
        log("❌ Cannot read device number.")
        return None

def fetch_url(device_number):
    try:
        response = requests.get(URL_ENDPOINT.format(device_number), timeout=10)
        return response.text.strip()
    except Exception as e:
        log(f"❌ Error fetching URL: {e}")
        return None

def write_url(url):
    try:
        with open(URL_FILE, "w") as f:
            f.write(url)
        log(f"📤 URL written to file: {url}")
    except Exception as e:
        log(f"❌ Failed to write file: {e}")

def main():
    log("🚀 URL fetcher started...")
    last_url = ""
    device_number = get_device_number()
    if not device_number:
        return

    while True:
        current_url = fetch_url(device_number)
        if current_url and current_url != last_url:
            last_url = current_url
            write_url(current_url)
        else:
            log("✅ No change in URL.")
        time.sleep(5)

if __name__ == "__main__":
    main()
