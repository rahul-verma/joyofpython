'''
This file is a part of The Joy of Python Gihub Repository.
Copyright 2019 Rahul Verma
Website: www.RahulVerma.net
Email: rv [at] testmile.com
Creator: Rahul Verma
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import time
import re
from subprocess import Popen, PIPE

from jopt.os_utils import *


def execute_command(*command_parts):
    proc = Popen(command_parts, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')
    return proc.pid, stdout, stderr


def find_process_ids(proc_name_pattern):
    command = None
    if is_windows_os():
        command = ('cmd', '/C', 'tasklist')
    else:
        command = ('top', '-l', '1')

    pid, stdout, stderr = execute_command(*command)
    return re.findall(proc_name_pattern, stdout)


def launch_nonblocking_process(command, wait_time=5):
    # Facing unresolvable issues with pexpect to launch chromedriver.
    # For the time being, a hacked solution.

    proc = Popen(command, stdout=PIPE, stderr=PIPE)
    time.sleep(wait_time)
