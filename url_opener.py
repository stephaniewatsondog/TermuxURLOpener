import requests
import subprocess
import time

# URL of your server that returns the latest URL to open
URL_ENDPOINT = "https://tools.cognitechs.org/urlopner/latest"

def get_latest_url():
    try:
        response = requests.get(URL_ENDPOINT, timeout=10)
        if response.status_code == 200:
            url = response.text.strip()
            if url.startswith("http"):
                return url
    except Exception as e:
        print(f"Error fetching URL: {e}")
    return None

def open_url_on_device(url):
    print(f"Opening URL: {url}")
    subprocess.run([
        "am", "start", "-a", "android.intent.action.VIEW", "-d", url
    ])

def main():
    last_url = ""
    while True:
        current_url = get_latest_url()
        if current_url and current_url != last_url:
            open_url_on_device(current_url)
            last_url = current_url
        time.sleep(5)

if __name__ == "__main__":
    main()
