# To generate wallpapers

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def create_wallpaper(img_path, output_path, title):
    img = Image.open(img_path).convert("RGB")

    # Screen Size 
    SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080

    #To Blur the Wallpaper
    bg = img.copy()
    bg = bg.resize((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = bg.filter(ImageFilter.GaussianBlur(25))

    # To center the main image 
    img.thumbnail((SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.7))
    offset_x = (SCREEN_WIDTH - img.width) // 2
    offset_y = (SCREEN_HEIGHT - img.height) // 2

    bg.paste(img, (offset_x, offset_y))

    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype("assets/fonts/Roboto-VariableFont_wdth,wght.ttf", 60)

    draw.text((50, SCREEN_HEIGHT - 120), title, fill="white", font=font)

    bg.save(output_path)

    bg.save(output_path)
    return output_path