import io
from pathlib import Path
import subprocess
import requests
import PIL.Image
import PIL.ImageFilter

# display resolution
width, height = 1440, 900

# x2 for better look (because jpg)
width  *= 2
height *= 2

img_file = Path('blur.jpg').absolute()

_ = f'https://source.unsplash.com/random/{width}x{height}'
_ = requests.get(_).content
_ = io.BytesIO(_)
_ = PIL.Image.open(_)
_ = _.filter(PIL.ImageFilter.GaussianBlur(radius=60))
_.save(img_file)

set_wallpaper = f'''
tell application "System Events"
    tell every desktop
        set picture to "{img_file}"
    end tell
end tell
'''

subprocess.run(['osascript', '-e', set_wallpaper])
subprocess.run(['killall', 'Dock']) # sometimes you need this
