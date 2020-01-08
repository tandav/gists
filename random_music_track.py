from pathlib import Path
import random
import plistlib
import webbrowser

music = Path('/Users/tandav/Documents/spaces/music/music')
tracks = list(music.rglob('*.webloc'))

track = random.choice(tracks)
print(track.relative_to(music))
with open(track, 'rb') as fd:
    url = plistlib.load(fd)['URL']
webbrowser.open(url)
