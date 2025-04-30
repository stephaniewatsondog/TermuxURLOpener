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
            # Find <div> with "Latest URL:"
            divs = soup.find_all("div")
            for div in divs:
                if "Latest URL:" in div.text:
                    url = div.text.split("Latest URL:")[1].strip()
                    if url.startswith("http"):
                        print(f"[INFO] Fetched new URL: {url}")
                        return url
    except Exception as e:
        print(f"[ERROR] Failed to fetch URL: {e}")
    return None

def open_url_on_device(url):
    print(f"[INFO] Opening URL: {url}")
    subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url])

def main():
    last_url = ""
    while True:
        current_url = get_latest_url()
        if current_url and current_url != last_url:
            open_url_on_device(current_url)
            last_url = current_url
        else:
            print("[INFO] No new URL found or already opened.")
        time.sleep(5)

if __name__ == "__main__":
    main()
