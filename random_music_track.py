from pathlib import Path
import random
import plistlib
import webbrowser
import sys

if len(sys.argv) == 2:
    music = Path(sys.argv[1])
else:
    music = Path('/Users/tandav/Documents/spaces/music/music')

print(music.absolute())

tracks = list(music.rglob('*.webloc'))

track = random.choice(tracks)
print(track.relative_to(music))
with open(track, 'rb') as fd:
    url = plistlib.load(fd)['URL']
webbrowser.open(url)