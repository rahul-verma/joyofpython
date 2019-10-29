
## 3. Launching and Handling Child Processes

- [Understanding Regular Expressions](#understanding-regular-expressions)
- [Hands-On: Matching and Extraction in one-go](#hands-on-matching-and-extraction-in-one-go)
- [Checking operating system at run-time](#checking-operating-system-at-run-time)
- [Exercise](#exercise)
- [The `subprocess` module](#the-subprocess-module)
- [Specifying Varible Number of (Positional) Arguments in a Function Call](#specifying-varible-number-of-positional-arguments-in-a-function-call)
- [Hand-On: Get Directory listing and print the output](#hand-on-get-directory-listing-and-print-the-output)
- [Exercise: Find Process ID(s) Based On Process Name Regex Pattern](#exercise-find-process-ids-based-on-process-name-regex-pattern)
  * [Tips and Inputs](#tips-and-inputs)
- [Hands-On (For Mac-Linux) and Demo-Only for Windows: Parent in Non-Blocking Mode using pexpect](#hands-on-for-mac-linux-and-demo-only-for-windows-parent-in-non-blocking-mode-using-pexpect)
- [Demo and Walk-through: Automating Chrome using requests, JSON Wire Protocol and chromedriver](#demo-and-walk-through-automating-chrome-using-requests-json-wire-protocol-and-chromedriver)
  * [Critical Information about Protocol](#critical-information-about-protocol)
  * [Tips and Inputs](#tips-and-inputs-1)

### Understanding Regular Expressions

Regular Expressions provide you with a vast grammar for string searching, matching and extraction.

For most common scenarios, knowing the following part of grammar is sufficient:

```
[chars] - Allowed characters
\w - word    \W  Non-word
\d - digit   \D  Non-digit
\s - space   \S  Non-space
.  - anything

Ocurrences
{min, max}
*  0 or more times
+  1 or more times
?  0 or 1 time

For extraction:
Mark a group using parenthesis: ()
```

### Hands-On: Matching and Extraction in one-go

Python's built-in `re` module helps you in doing all stuff related to regular expressions.

For the purpose of this exercise, we will extract parts of a string based on pattern matching.

```python
re.match(pattern, target_string)
```

Let's implement the function `extract_email_parts` in `data_utils.py` file to extract the email id and domain when an email address is provided.

We'll call the function in `ex13.py` and validate output.

### Checking operating system at run-time

At times, you need to determine the OS name at run time to take OS-specific actions.

Using `platform` module's `system()` call, you can check the current operating system name.

```python
platform.system()
```

### Exercise

1. Implement `is_windows_os` function in `os_utils.py`.
2. Call the function in `ex14.py` to validate output.

### The `subprocess` module

Python has a built-in `subprocess` module using which you can launch child processes.

```python
from subprocess import Popen, PIPE
```

Let's say there is a command `proc_name -a -b 2` that you want to launch. Also, you want to capture the output of pipes (STDOUT/STDERR) as bytes.

On Mac/Linux, you can launch it as follows:
```python
proc = Popen(['proc_name`, '-a', '-b', '2'], stdout=PIPE, stderr=PIPE)
```

On Windows, you can launch it as follows:
```python
proc = Popen(['cmd', '/C', 'proc_name`, '-a', '-b', '2'], stdout=PIPE, stderr=PIPE)
```

To capture the output of pipes, you can use the `communicate` method:

On Windows, you can launch it as follows:
```python
stdout, stderr = proc.communicate()
```

### Specifying Varible Number of (Positional) Arguments in a Function Call

You can specify variable number of args for a function using the following syntax:

```python
def some_function(a, b, *args):
    function body
    In the body args is available as a tuple.
```

### Hand-On: Get Directory listing and print the output

On Mac/Linux, use:
```
ls -l
```

On Windows, use:
```
dir
```

Let's implement the `execute_command` function in `process_utils.py`.

We'll call the function in `ex15.py` and validate output.

### Exercise: Find Process ID(s) Based On Process Name Regex Pattern

1. Implement the `find_process_ids` function in `process_utils.py` file. It takes the process name pattern, runs the appropriate command as per a platform and then extracts the process ids.
2. Call the function in `ex16.py` and validate output.

#### Tips and Inputs
1. You can use `re.findall(pattern, target_string)` to find all matches.
2. `top -l 1` is the command that you can run on Mac/Linux to find the processes. The first column contains the process ids and the second contains the process names.
3. `tasklist` is the command that you can use on Windows. The first column is the process name and the second column is the process id.
4. `communicate()` call returns output as byte-string. Before you can do text-operations/regex matching on the output, you need to decode it. For example, `stdout.decode('utf-8')`

### Hands-On (For Mac-Linux) and Demo-Only for Windows: Parent in Non-Blocking Mode using pexpect

There are child processes which you would want to interact with post launching. This could be a trickly task on Windows. However, on Mac/Linux this is made very approachable using `pexepct` module.

Considering the basic nature of this workshop, this section has been kept shorter.

(For those on Mac/Linux), let's launch Python interactive shell from Python Interactive Shell. We will interact between these parent and child shells using pexpect.

```python
>>> import pexpect
>>> child = pexpect.spawn('python3')
>>> child.expect('>>>')
>>> child.before
>>> child.sendline('import math')
>>> child.expect('>>>')
>>> child.before
>>> child.sendline('math.sqrt(4)')
>>> child.expect('>>>')
>>> child.before
>>> 
```

### Demo and Walk-through: Automating Chrome using requests, JSON Wire Protocol and chromedriver

ChromeDriver executable can be used to automate Chrome. As a part of this demonstrate to you the following steps:

1. Launch Chrome.
2. Go to `https://www.google.com`.
3. Find all HTML nodes with the tag `input` and print the source.
4. Quit Chrome.

Following information is provided for you in case you would like try out doing it on your own after the workshop.

#### Critical Information about Protocol

1. When launching the executable provide `--port=4322` as argument. Once launched, the process would create a web service listening at port 4322. This service can then be accessed at the url: `http://localhost:4322`
2. You can launch chrome by sending a POST request to the url `http://localhost:4322/session`. The content/body to be sent as a part of this request is available as `launch_chrome.json` file in `input` directory of project.
3. The step 2 will return a JSON response from which you can extract the session-id. For example `response['value']['sessionId']`. Let's call it `session_id`.
4. To go to a URL, send a POST request to `http://localhost:4322/session/<session_id>/url` with the JSON body: `{'url' : '<url>'}`.
5. To get page source, send GET request to `http://localhost:4322/session/<session_id>/source`. The source is contained in 'value' attribute.
6. To quit browser, send DELETE request to `http://localhost:4322/session/<session_id>`.

Launch "ChromeDriver" as a sub-process in a non-blocking mode. 

#### Tips and Inputs
1. On Mac/Linux, use `subprocess` or `pexepct` as per comfort. On Windows, use `subprocess` module. While using `subprocess` use `time.sleep(3-4 seconds)` call as a hack.
2. Continue the legacy of dynamic paths, by implementing `get_driver_path` in `project_utils.py` file. 
3. The name of executable contains `.exe` extension for Windows. Handle this using using the cross-platform technique taught earlier.
