import requests
import subprocess
import time
from bs4 import BeautifulSoup

URL_PAGE = "https://tools.cognitechs.org/urlopner/"

def get_latest_url():
    try:
        response = requests.get(URL_PAGE, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            strong_tags = soup.find_all("strong")
            for tag in strong_tags:
                if "Latest URL:" in tag.text:
                    url = tag.text.replace("Latest URL:", "").strip()
                    if url.startswith("http"):
                        return url
    except Exception as e:
        print(f"[❌ ERROR] Failed to fetch URL: {e}")
    return None

def open_url_on_device(url):
    print(f"[✅ OPENING] URL: {url}")
    subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url])

def main():
    last_url = ""
    print("🔁 [RUNNING] Watching for new URL every 5 seconds...\n")
    while True:
        print("🔍 Checking for new URL...")
        current_url = get_latest_url()
        if current_url and current_url != last_url:
            print(f"🆕 New URL found: {current_url}")
            open_url_on_device(current_url)
            last_url = current_url
        else:
            print("⚠️ No new URL or same as last.")
        print("⌛ Waiting 5 seconds...\n")
        time.sleep(5)

if __name__ == "__main__":
    main()
