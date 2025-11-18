from apod import get_apod, download_image
from wallpaper import create_wallpaper
from utils import set_wallpaper_mac
import os
from datetime import date

def main ():
    info = get_apod()
    title = info["title"]
    img_url = info["url"]

    filename = f"output/wallpapers/{date.today()}_apod.jpg"
    os.makedirs("output/wallapers", exist_ok=True)

    img_path = download_image(img_url, filename)
    wallpaper_path = create_wallpaper(img_path, filename, title)
    
    set_wallpaper_mac(wallpaper_path)
    print("Wallpaper has been Updated Successfully")

    if __name__ == "__main__":
        main()