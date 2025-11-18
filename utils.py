# This file is for the helper functions

import os 
# To set the wallper for a mac
def set_wallpaper_mac(path):
    os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \'{path}\"'")

# For Windows 
#import ctypes

#def set_wallpaper_windows(path):
#    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

# For Linux 
#def set_wallpaper_linux(path):
#    os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}'")
