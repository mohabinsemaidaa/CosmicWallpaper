# 🌌 CosmicWallpaper

![CosmicWallpaper Banner](https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1950&q=80)

**CosmicWallpaper** is a Python project that automatically fetches NASA’s Astronomy Picture of the Day (APOD) and generates an **aesthetic, high-resolution wallpaper** for your desktop. It adds a blurred background, centers the image, overlays the title, and optionally sets it as your Mac wallpaper daily.

---

## ✨ Features

- Fetches NASA APOD daily images with title and description.
- Automatically resizes images to your screen resolution.
- Creates a visually appealing wallpaper with:
  - Blurred background
  - Centered main image
  - Title overlay
- Saves wallpapers locally for archival.
- Automatically sets wallpaper on **macOS**.
- Lightweight and easy to customize.

---

## 🛠️ Technology & Libraries

- **Python 3.10+**
- [Pillow](https://pillow.readthedocs.io/) – image processing
- [Requests](https://docs.python-requests.org/) – API requests
- [python-dotenv](https://github.com/theskumar/python-dotenv) – environment variable management
- NASA APOD API

---

## 🖥️ Installation

1. Clone the repository:

```bash
git clone https://github.com/mohabinsemaidaa/CosmicWallpaper.git
cd CosmicWallpaper
```

2. Create a Python virtual environment:

```bash 
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Add you NASA API key in a .env file
```
API_KEY = NASA_API_KEY
```
### ⚠️ Disclaimer

This project uses a NASA API key stored in a `.env` file.  
**Do not commit your `.env` file to GitHub** — it is already included in `.gitignore`.  
Exposing your API key publicly may result in misuse or API limit issues.


## Usage

```bash 
python main.py
```
This will:
- Fetch today’s APOD image.

- Create a wallpaper with blurred background + title overlay.

- Save it to output/wallpapers YYYY-MM-DD_apod.jpg.

- Automatically set it as your wallpaper on macOS.

## Screenshots

Nothing for now since on the day this was completed the media type released today was a video

## Cross-platform Notes

- MacOS: Fully supported with automatic wallpaper setting
- Windows: Wallpaper can be set using **ctypes**. See **utils.py**
- Linux (GNOME): Wallpaper can be set via **gsettings**. See **utils.py**
- Other Linux desktops: Manual wallpaper change my be required.

## Optional Features

- Schedule daily updates with cron (MacOS/Linux) or Task Scheduler (Windows).
- Customize wallpaper size for different resolutions.

## Resources 

- NASA APOD API: https://api.nasa.gov/
- Pillow Documentation: https://pillow.readthedocs.io/
- Python Requests: https://docs.python-requests.org/

## License 

MIT License - feel free to use, modify, and share.