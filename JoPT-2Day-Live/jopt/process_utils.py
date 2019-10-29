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


def execute_command(*command_parts):
    pass


def find_process_ids(proc_name_pattern):
    pass


def launch_nonblocking_process(command, expected_match):
    proc = Popen(command, stdout=PIPE, stderr=PIPE)
    # Handling non-blocking process is a more involved game.
    time.sleep(2)
    output = proc.stdout.read().decode("utf-8")

    match = re.search(expected_match, output)
    if not match:
        raise Exception(proc.stderr.read().decode("utf-8"))

    print(output)


'''
On non-Windows systems, one can use pexpect module for better experience.
>>> import pexpect
>>> c = pexpect.spawn('python3')
>>> c.expect('>>>')
0
>>> c.before
b'Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) \r\n[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin\r\nType "help", "copyright", "credits" or "license" for more information.\r\n'
>>> c.after
b'>>>'
>>> c.sendline('dir')
4
>>> c.expect('>>>')
0
>>> c.before
b' dir\r\n<built-in function dir>\r\n'
>>> c.sendline('dir()')
6
>>> c.before
b' dir\r\n<built-in function dir>\r\n'
>>> c.after
b'>>>'
>>> c.expect('>>>')
0
>>> c.before
b" dir()\r\n['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']\r\n"
>>> c.sendline('dir(__builtins__)')
18
>>> c.expect('>>>')
0
>>> c.before
b" dir(__builtins__)\r\n['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']\r\n"
>>> 
'''