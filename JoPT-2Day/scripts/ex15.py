from jopt.process_utils import *

# For mac ls -l. For windows: cmd /C dir
pid, stdout, stderr = execute_command('ls', '-l')

print(stdout)
print(stderr)
