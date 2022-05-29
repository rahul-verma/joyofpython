
## 3. Launching and Handling Child Processes

- [Understanding Regular Expressions](#understanding-regular-expressions)
- [Hands-On: Simlutaneous-String-Matching and Extraction](#hands-on-simlutaneous-string-matching-and-extraction)
- [Checking operating system at run-time](#checking-operating-system-at-run-time)
- [Exercise](#exercise)
- [The `subprocess` module](#the-subprocess-module)
- [Specifying Variable Number of (Positional) Arguments in a Function Call](#specifying-variable-number-of-positional-arguments-in-a-function-call)
- [Hand-On: Get Directory Listing and Print the Output](#hand-on-get-directory-listing-and-print-the-output)
- [Exercise: Find Process ID(s) Based On Process Name Regex Pattern](#exercise-find-process-ids-based-on-process-name-regex-pattern)
  * [Tips and Inputs](#tips-and-inputs)
- [Hands-On (For Mac-Linux) and Demo-Only for Windows: Parent in Non-Blocking Mode using `pexpect` Module](#hands-on-for-mac-linux-and-demo-only-for-windows-parent-in-non-blocking-mode-using-pexpect-module)
- [Demo and Walk-through: Automating Chrome using requests, JSON Wire Protocol and chromedriver](#demo-and-walk-through-automating-chrome-using-requests-json-wire-protocol-and-chromedriver)
  * [Critical Information about Protocol](#critical-information-about-protocol)
  * [Tips and Inputs](#tips-and-inputs-1)

### Understanding Regular Expressions

Regular Expressions provide you with a vast grammar for string searching, matching and extraction.

For most common scenarios, knowing the following part of grammar is sufficient:

```
[chars] - Allowed characters
\w - [a-zA-Z0-9_]    \W  Opposite
\d - [0-9]           \D  Opposite
\s - space           \S  Opposite
.  - anything

Ocurrences
{min, max} - min to max times
*  0 or more times
+  1 or more times
?  0 or 1 time

For extraction:
Mark a group using parenthesis: ()
```

### Hands-On: Simlutaneous String Matching and Extraction

Python's built-in `re` module helps you in doing all stuff related to regular expressions.

For the purpose of this exercise, we will extract parts of a string based on pattern matching.

```python
re.match(pattern, target_string)
```

**Tip** As regex patterns often contain `\x` nature of constructs and `\` is used to mark escape sequences in strings e.g. `\n`, we need to handle this. One option is to escape the backslash `\\`. This is what you do in most languages. Python gives a much cleaner way with its `raw-string` type. Prefix a string with the letter `r` to make it a raw-string: `r"sample-string"`.

Let's implement the function `extract_email_parts` in `data_utils.py` file to extract the email id and domain when an email address is provided.

We'll call the function in `ex13.py` and validate output.

### Checking operating system at run-time

At times, you need to determine the OS name at run time to take OS-specific actions.

Using `platform` module's `system()` call, you can check the current operating system name.

```python
import platform
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

On Windows, you can launch it as follows (`/C` is provided so that the `cmd` process exists once command has completed its execution.):
```python
proc = Popen(['cmd', '/C', 'proc_name`, '-a', '-b', '2'], stdout=PIPE, stderr=PIPE)
```

To capture the output of pipes, you can use the `communicate` method:

```python
stdout, stderr = proc.communicate()
```

### Specifying Variable Number of (Positional) Arguments in a Function Call

You can specify variable number of args for a function using the following syntax:

```python
def some_function(a, b, *args):
    function body
    In the body args is available as a tuple.
```

### Hand-On: Get Directory listing and Print the Output

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
2. `top -l 1` command (one iteration) can be used on Mac to find the running processes. The first column contains the process ids and the second contains the process names.
3. `top -b -n 1` command (batch mode, 1 iteration) can be used on Linux. The first column contains the process ids and the last column contains the process name.
4. `tasklist` is the command that you can use on Windows. The first column is the process name and the second column is the process id.
5. `communicate()` call returns output as byte-string. Before you can do text-operations/regex matching on the output, you need to decode it: `stdout.decode('utf-8')`
