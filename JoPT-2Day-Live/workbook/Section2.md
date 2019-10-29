## Section 2. Basic Web Service Requests and File Handling

- [Installing PyPi packages using pip](#installing-pypi-packages-using-pip)
- [Simple GET Request](#simple-get-request)
- [Hands-on - Fetching JSON Content using a basic GET request.](#hands-on-fetching-json-content-using-a-basic-get-request)
- [Hands-on - Finding Project Root Directory at Run-time](#hands-on-finding-project-root-directory-at-run-time)
- [Exercise: Reading and Writing Text Files](#exercise-reading-and-writing-text-files)
- [Hands-On: Reading and Writing a File](#hands-on-reading-and-writing-a-file)
- [Hands-On: String methods - `split` and `join` and Optional Arguments in Functions](#hands-on-string-methods---split-and-join-and-optional-arguments-in-functions)
- [Hands-On: `zip` and `dict` built-in functions](#hands-on-zip-and-dict-built-in-functions)
- [Long Exercise: Reading and Writing Delimited and JSON Files](#long-exercise-reading-and-writing-delimited-and-json-files)
- [Walk-through of a Sample Solution: Reading and Writing Delimited and JSON Files](#walk-through-of-a-sample-solution-reading-and-writing-delimited-and-json-files)
- [Demo and Walk-through: Reading and Writing XML Files](#demo-and-walk-through-reading-and-writing-xml-files)
- [Demo: Simple SOAP POST Request](#demo-simple-soap-post-request)
  
### Installing PyPi packages using pip

Beyond the packages that come pre-installed, you can also intall packages of choice from thousands of packages available on Python Package Index (PyPi). Run the following command from terminal:

```pip install requests```

Here we are installing `requests` module which is the most popular Python library for interacting with web services.

### Simple GET Request

Web services mostly work on HTTP and the most common HTTP methods used by web services are GET, POST, PUT, DELETE.

A GET request can be sent easily:

```python
import requests
response = requests.get(<url>)
```

If you know that the response contains JSON response, you can convert get it as a Python dictionary:

```python
json = response.json()
```

### Hands-on: Fetching JSON Content using a basic GET request.
Code should be implemented in `ex07.py`.

Send a GET request to the url `https://jsonplaceholder.typicode.com/posts`. From the response, print the title of the first 10 post records.

### Hands-on: Finding Project Root Directory at Run-time

Python has pre-defined magic attributes, also called dunder attributes (doublw underscore attributes) for various types of object. One such attribute is `__file__` attribute which gives the path of current file.

Built-in `os` module has various functions which are useful to a tester:

```python
os.path.dirname # to extract directory part from a file path
os.path.realpath # convert a relative path to canonical/full path
os.path.join  # to create a full path from parts by using a cross-platform path separator
```

Let's implement the `get_root_dir()` function in `project_utils.py` file in `jopt` package.

Call the function and validate the output in `ex08.py`.

### Exercise: Reading and Writing Text Files

1. Create `output` directory in project root.
2. In `project_utils.py`, implement the `get_input_file_path` and `get_output_file_path` functions to dynamically build paths for files present in the `input` and `output` directories by providing the `file_name` argument.
3. Make calls to these functions in `ex08.py` to validate the output.

### Hands-On: Reading and Writing a File

```python
f = open("<file_path>", "r") # Opens the file and returns a file object
f.read() # Reads all the content
f.close() # closes the file handle
```

Following calls can be used to create and write to a file:
```python
f = open("<file_path>", "w") # Opens the file and returns a file object
f.write(<string>) . # Write a string a to the file
f.close() # closes the file handle
```

For automatically closing a file when the job is done, you can also use the `with` block:

```python
with <open_command> as <file_object>:
    Read/Write content

# When the control comes out of block, the file handle is closed.
```

1. Let's implement the `write_file` function in `file_utils.py`. Utilize the `get_output_file_path` in `project_utils` to create full file path.
2. In `ex09.py` call the function to write some content.
3. Implement the `read_file` function in `file_utils.py`. Utilize the `get_input_file_path` in `project_utils.py` to create full file path.
4. In `ex09.py`, pass the same file name used in step 2 and validate that expected content is read.

### Hands-On: String methods - `split` and `join` and Optional Arguments in Functions

For splitting a string based on a delimiter and for joining a sequence of strings based on a delimiter, following string methods come handy:
```python
"a,b,c".split(",") . # Can use any delimiter
",".join(['a', 'b', 'c'])
```

Python supports optional/default arguments in functions i.e. if you don't pass the argument while calling, the default value of the argument is consumed. In the function definition, you can specifiy it as follows (here `b` is the optional argument):
```python
def some_function(a, b=<default>):
    function body
```

1. Let's implement the `list_to_str` and `csv_str_to_list` functions in `data_utils.py` file.
2. `delimiter` should be an optional argument.
3. Call the functions in `ex10.py` file and validate.

### Hands-On: `zip` and `dict` built-in functions

Python's `zip` function can be used to combine sequences into a nested sequence where each element is a tuple of corresponding indexed elements in the sequences provided.

```python
zip([1,2], [3,4]) # returns ((1,3),(2,4))
```

`dict` function can take a specific style of nested sequence as an argument where each element is a 2-element tuple and convert it into a dictionary.

```python
dict((1,3),(2,4)) # returns {1:3, 2:4}
```

1. Let's implement the `convert_to_map` function in `data_utils.py` file.
2. Call the function in `ex11.py` file and validate.

### Long Exercise: Reading and Writing Delimited and JSON Files
The `ex12_csv_json_files.py` should be considered as the main python file. Beyond this constraint, feel free to create and use modules as you find appropriate.

1. Send a GET request to the url 'https://jsonplaceholder.typicode.com/users'.
2. From the response remove the 'address' and 'company' attributes of each user.
3. Write the data for the first 10 users in a CSV file as well as a JSON file.
4. Read the data from this generated CSV file. Let's call it `csv_output`.
5. Read the data from the generated JSON file. Let's call it `json_output`.
6. Compare that the user names are same for all users in `csv_output` and `json_ouput`

Hints
1. Use the constructs that we created so far.
2. Use `\n` as the new line character when ending a line or when joining multiple lines. `os.linesep` is a cross-platform line separator, but used internally by Python when reading content.
3. You can experiment with `readline`, `readlines`, `writelines` methods of file handle.

### Walk-through of a Sample Solution: Reading and Writing Delimited and JSON Files
Let's look at the details of a possible solution. Map to the way you approached the problem and take a note of any new learning or a different way of solving the same problem.

### Demo and Walk-through: Reading and Writing XML Files
As this is a 2-day workshop, dealing with XML files is not done in a hands-on mode. The purpose is to quickly show you the relevant pieces of building blocks for XML creating and parsing in Python.

### Demo: Simple SOAP POST Request
As this is a 2-day workshop, dealing with XML files is not done in a hands-on mode. The purpose is to quickly show you the relevant pieces of building blocks for XML creating and parsing in Python.
