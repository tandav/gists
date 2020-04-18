import subprocess

def notification(title, subtitle, text):
    code = f'display notification "{text}" with title "{title}" subtitle "{subtitle}"'
    cmd  = 'osascript', '-e', code
    subprocess.run(cmd)
