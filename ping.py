import subprocess
import time
import shlex
import re
import macos


router = subprocess.check_output('route get default | grep gateway', shell=True, text=True).strip().split()[1]
cmd = f'sudo ping -f {router} -c 999'
cmd = shlex.split(cmd)

pattern = r'[\d|\.]+(?=%)'

NOTIFICATION_TRESHOLD = 50 # %

while True:
    out = subprocess.check_output(cmd, text=True)
    a, b = out.splitlines()[-2:]
    print(b, a, sep=' | ')
    loss = float(re.search(pattern, a).group())

    if loss > NOTIFICATION_TRESHOLD:
        macos.notification(text=f'{loss}%', title='poor connection', subtitle='packet loss')

