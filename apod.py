# apod.py — Fetching NASA APOD data

import requests
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("NASA API_KEY not found. Add it to your .env file.")

# Fetch today’s APOD data
def get_apod():
    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
        data = requests.get(url).json()

        # Check if APOD is an image
        if data.get("media_type") != "image":
            print("Today’s APOD is a video. Skipping download.")
            return None

        return {
            "title": data.get("title"),
            "explanation": data.get("explanation"),
            "url": data.get("url")
        }

    except Exception as e:
        print("Error fetching APOD:", e)
        return None

# Download image from URL
def download_image(img_url, save_path):
    try:
        img_data = requests.get(img_url).content
        with open(save_path, "wb") as f:
            f.write(img_data)
        print(f"Image downloaded successfully: {save_path}")
        return save_path
    except Exception as e:
        print("Error downloading image:", e)
        return None

# Debug: test fetching
if __name__ == "__main__":
    apod = get_apod()
    if apod:
        print("Title:", apod["title"])
        print("URL:", apod["url"])
        download_image(apod["url"], "test_apod.jpg")
