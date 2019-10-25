import re

from jopt.process_utils import *

pid, stdout, stderr = execute_command("ls", "-l")
pattern = r'\s+(\w+\.py)'

matches = re.findall(pattern, stdout)
for match in matches:
    print(match)

'''
For Windows
cmd.exe 
/K Remains
/C exits
'''

