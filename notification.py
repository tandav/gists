import subprocess

def notification(text=None, title=None, subtitle=None):
    code = f'display notification "{text}"' 
    if title:
        code += f'with title "{title}"'
    if subtitle:
        code += f'subtitle "{subtitle}"'
    cmd  = 'osascript', '-e', code
    subprocess.run(cmd)
