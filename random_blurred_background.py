import io
import pathlib
import subprocess
import requests
import PIL.Image
import PIL.ImageFilter

# display resolution
width, height = 1440, 900

# x2 for better look (because jpg)
width  *= 2
height *= 2

img_file = pathlib.Path('blur.jpg').absolute()
print(img_file)

(
    PIL
    .Image
    .open(
        io
        .BytesIO(
            requests
            .get(f'https://source.unsplash.com/random/{width}x{height}')
            .content
        )
    )
    .filter(
        PIL
        .ImageFilter
        .GaussianBlur(radius=60)
    )
    .save(img_file)
)

set_wallpaper = f'''
tell application "System Events"
    tell every desktop
        set picture to "{img_file}"
    end tell
end tell
'''

subprocess.run(['osascript', '-e', set_wallpaper])
