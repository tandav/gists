import subprocess
import sys


print('================================')

old_commit, new_commit, ref = sys.stdin.read().split()

_, branch = ref.rsplit('/', maxsplit=1)

print('old_commit:', old_commit)
print('new_commit:', new_commit)
print('ref:', ref)

subprocess.check_output(['git', '--work-tree', '..', '--git-dir', '.', 'checkout', '-f', branch])
subprocess.check_output(['git', 'show', '--stat', new_commit])

# place there other build commands
print('deployed successfully')
print('================================')
