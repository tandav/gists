import subprocess
import time
import shlex

router = subprocess.check_output('route get default | grep gateway', shell=True, text=True).strip().split()[1]
cmd = f'sudo ping -f {router} -c 999'
cmd = shlex.split(cmd)

while True:
    out = subprocess.check_output(cmd, text=True)
    a, b = out.splitlines()[-2:]
    print(b, a, sep=' | ')
