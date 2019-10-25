## The Joy of Python for Testers - Workbook for 2-day version

### Purpose
The primary purpose of this document and related code examples is to act as accompanying material to the workshop by Rahul Verma. 

It contains the primary pieces of information building blocks as per the flow of the workshop. So, it provides supporting pieces for the workshop.

The workhop encourages the participants to continue practising Python after the workshop. So, a seocndary and yet very important purpose of this content is to enable the participants to go through the learning on their own by coding the exercises without interruption.

### 1. Python Fundamentals

#### Fundamental Python Constructs

We are going to use Python Interactive Shell for this section.

Python is losely typed language. Type of a variable (referred to as a name) is essentially the type of object it points to.

```python
>>>a = 1
>>>f = 1.1
>>>b = True
```

Names in Python mostyle follow these rules (for variables, functions/methods, modules, packages - i.e. most of the names):
  - Contain letters, numbers and underscore `_`
  - Can not start with a number
  - All letters in lower case (except global vars, constants etc where all uppercase letters are used.)
  - Multiple words separated by an underscore `_`
  - Underscore at the beginning of the name has special meaning. More on this later.

As the left hand side in the assignment is just a name without a type of its own, it can be assigned to an object of another type. Remember that this is, in general, not suggested. There are specific situations where it comes handy, which we would cover in the workshop.

```python
>>>b = 1
```

You don't need to worry about size of numbers in Python.
```python
>>>a = 11111111111236723546735467235476235467523475234675236745237452376452376452374527354573
```

Python provides 2 types of sequential containers.

First one is a `list` which is a variable size container, without you worrying about the size.
```python
>>>l = [1, 2, 3]
```

Second seqquence type is `tuple`.
```python
>>>t = (1, 2, 3)
```

Sequences support index based retrieval of items. Index follows computer counting and starts from 0.
```python
>>>l[0]
>>>t[0]
```

Lists are mutable. Tuples are immutable. Here the second statement would throw an exception.
```python
>>>l[0] = 5
>>>t[0] = 5
```

Strings can be defined in Python using single or double quotes.
```python
>>>s = "testing"
>>>s = 'testing'
```

Strings are sequences too. Each character is an item.
```python
>>>s[0]
```

Strings are immutable.
```python
>>>s[0] = 'r'
```

Python has a built-in mapping data type called `dict` (short for dictionary). 
```python
>>>d = {1: 2, 3: 4}
```

You can retrieve an item from a dictionary by using corresponding key. Syntax is similar to sequence's index based retrieval.
```python
>>>d[1]
```

Python has a built-in `set` type as well.
```python
>>>s1 = {1,2,3}
```

As both dictionary and set use curly braces `{}`, as markup, to declare an empty set you need a `set()` call.
```python
>>>s2 = set()
```

Python supports the usual operators like other languages `+, -, *, %`
```python
>>>1+1
```

Python has 2 different division operators `/` and `//` to cater to 2 different needs.
```python
>>>1/3
>>>1//3
```

Python uses `**` as the exponentiation (power) operator.
```python
>>>3 ** 2
```

Python supports augmented operators. E.g. instead of `a = a+1`, you can do the following:
```python
>>>a = 1
>>>a += 1
>>>a
```

Python supports familiar relational operators to compare basic types: `==,>, <, <=, >=, !=` 
```python
>>>a = 1
>>>a == 1  # are others
```

For containers, the bejavior is based on other factors. For example for sequences, each element is compared in order. Size comes next.
```python
>>>[10,3] > [2,3,4,5,6,7]
>>>[2,3] > [2,3,4,5,6,7]
```

Python support both procedural and object-oriented styles of programming.

Many built-in functions are available without any imports when the Python Interpreter loads.

Calling a Python function is similar to most languages.
```python
>>>print("Hello")
```

You can check type of an object using the built-in `type` function.
```python
>>>type(1)
```

You can chain function calls.
```python
>>>print(type(1))
```

There is a special keyword `is` which can be used for relational operation is well (More on this later).

Here we use it for type checking.
```python
>>>type(1) is int
```

You can also convert an object to another object type if it is allowed. Here, the last conversion will throw an exception.
```python
str(1)
int("1")
int("test")
```

Everything is an object in Python - a concept which is at the heart of the language. The simple objects we created so far offer behaviors. These behaviors are just like functions but attached to a particular object's state. You can call a method by using the method resolution operator that is a `.` (dot).

Here, we are calling the `append` method of a list object to add another element to the list.
```python
>>>l1 = [4,3,5]
>>>l1.append(1)
>>>l1
```

#### Importing modules
Python is referred to as a batteries-included langauge. It means that there are lots and lots of modules installed along with the core Python installation. These don't get loaded by default into memory when Python interpreter is launched. You will need to explcitily import what you want to use.

You can import a module by using the `import` keyword.

```python
>>>import math
>>>math.sqrt(4)
```

You can also import selective names from a module to be directly used in your code.

```python
>>>from math import sqrt
>>>sqrt(4)
```

Python has other `import` variants some of which we will explore as the workshop unfolds.

#### Creating Python Project and Running Our First Script
We are using PyCharm as the default IDE here, but you can use a Python IDE that you are comfortable with).
  - Create Python Project
  - Copy all the contents of this directory in GitHub repository in the root directory of the project.
  
In the `ex01.py` script, add the following:

```python
print("The Joy of Python")
```

We can run the script using the IDE or from the terminal by running the command: `python ex01.py`.

#### Creating Basic Functions

Functions in Python are defined using the keyword `def`.

```python
def function_name(arg1, arg2):
  # Function body
  return object1
```

The critical part to notice is that Python marks blocks using indentation unlike curly braces or begin & end markers in other languages. In other languages, it is suggested that you indent a child block for readability. Python in this matter imposes it on you and the code does not run without proper indentation. Depending on your school of thought, you might like or disklike this.

You can indent using a tab or a fixed number of spaces. No agreement exists on which is better.

A function can take 0 or more arguments. The names 'arg1', 'arg2' etc are available as names within the function body. The function can return one or more objects. If no return statement is supplied, then it returns `None` (which is eqivalent of NULL in other languages)

Once defined, you can call this function just like built-in functions.
```python
ret_val = function_name(1, 'testing')
```

#### Conditional Control Structures

Python supports code blocks that get executed when a condition is True or False.

It uses the familiar `if` and `else` keywords. 

For chaining of conditions, i.e. the `else if` situation, rather than two separate keywords clubbed, Python has a special keyword - `elif`. 

You can nest conditional blocks as well. Just make sure of the correct indentation level.
```python

if condition1:
  #path1
elif condition2:
  #path2
else:
  if nested_condition:
     #path3
   else:
     #path4
```

#### Exercise
In the script `ex01.py`, create a function with name `calc_grade` which takes an score (number) as an argument and returns grade as string as per the following rules:
  - 'C' grade if score is 40 or lesser
  - 'B' grade if score is greater than 40 but up to 80
  - 'A' grade for score greater than 80
  
 Call and experiment.
 
#### Exercise: Creating a Package and Module
Multiple modules can reside inside a single `package`. A `package` is a directory/folder containing an `__init__.py` file.

In the project, you can see that there is a `jopt` package already created. In this package, various modules are present. One of them is `basics.py` which contains skeletons of various functions that you are going to implement one by one.

  - Copy the contents of `calc_grade` function that you have created to corresponding function in `basics.py`
  - In the `ex02.py` file, add the following contents and execute:

```python
from jopt.basics import *
grade = calc_grade(43)
print(grade)
```

#### Raising an Exception

Rather than returning an error code, in Python you usually raise/throw an exception object.

You can raise an exception in Python by creating an exception object. Python does not use the `new` keyword like other languages, so creation of an object looks like a function call.

You can raise an exception using the `raise` keyword.

```python
raise Exception("This didn't go well")
```

#### Exercise
Improve the `calc_grade` function to throw an exception when a non-number object is provided. Run the ex02.py script by providing non-numbers to evaluate the behavior.

#### `for` Loop

The most commonly used construct in Python is proably the one where you iterate on a container using a `for` loop:

```python
for element in elements:
  print(element)
```

Tip: Name lists as a plural name. It goes a long way in the readability of your for loops on lists.

Python's built-in function `range(limit)` generates numbers from 0 till limit-1. Hence it is a good way to generate indices, especially when you are iterating over a list:

```python
for index in range(len(elements)):
  print(elements[index])
```

There is an obvious impact on readability. One can use enumerate() call instead.

```python
for index, element in enumerate(elements):
  print(index, element)
```

#### Exercise
Implement the function `calc_grades` which takes numbers list argument and using a for loop prints grades for all the numbers in the list by calling `calc_grade` function.

Call the function in ex03.py.

#### Taking Input from Console

You can take input from console using the built-in `input()` function. Remember that it always returns a string, so you might have to use the type conversion functions before using the value.

Also, make wise use of the prompt argument.

```python
age = input("What's your age? ")
print(int(age))
```

#### Exercise
Implement the function with name `calc_grade_for_console_input` which takes a number from console as an input and prints its grade.

Call the function in ex04.py.

#### `while` Loop
Another style of loop which can be used in Python is a `while` loop. You use it when the decision to stop the loop is taken within the body of the loop. In short, use it when you don't know how any iterations should be executed.

```python
while condition:
  # do this
```

Here, the loop runs as long as the condition evaluates to True.

#### Exercise
Implement the function with name `calc_grades_for_console_input` which uses `while` loop to take numbers as inputs from console and prints the grade using `calc_grade_for_console_input` function call. The program should exit when user enters 'x' in lower or upper case.

Call the function in ex05.py

#### Exception Handling
Error handling based code usually relies on preventive checking of potential problems that could take place.

Exception handling on the other end, usually lets the problem take place and handles it at appropriate layers. This is a common found feature in all OOP languages.

Python supports a 4 block exception handling. Out of these, one tends to use only the `try` and `except` blocks most of the times.

```python
try:
  #try this block
except ExceptionName1 as e:
  # do this if exception of type ExceptionName1 was raised
except ExceptionName2 as e:
  # do this if exception of type ExceptionName2 was raised
else:
  # do this if no excpetion occured
finally:
  # do this always
```

#### Exercise
Modify the function `calc_grades_for_console_input` to include exception handling for the case where user enters a non-number. The goal is to let the program continue in case of invalid input by informing the user that it was an invalid input.

Call the function in ex05.py

#### Long Exercise - Put It All Together - The MindMaster Game
Create a MindMaster Game in `ex06_mindmaster.py`. You can treat it as the main script and create functions/modules the way you like. One thing to certainly avoid is writing a monolithic script.

##### Business Requirements
1. The Program thinks about a 3-digit number.
2. User is given 10 attempts to guess the number via Console/Terminal.
3. For each guess, user is provided feedback. The feedback mentions 2 things - how many digits are correct and how many digits are at correct position.
4. User is able to play the game any number of times.
5. After each game play, the program informs the user about how many games s/he won or lost.


##### Technical Requirements
1. Whether the number contains duplicate digits should be configurable.
2. User `format()` for string formatting instead of string concatenation using +.
3. Use a dictionary for storing number of games won and lost.
4. Handle and process exception for a non-int entry. It would be counted as an attempt.

##### Hints
1. When you convert a string to a list, each character is an item in the list.
2. `strip()` method of string removes the extraneous spaces at head as well as tail.
3. You can generate a random integer between a range by using `randint(x,y)` function in `random` module.

#### Walk-through of a Sample Solution

### 2. Basic Web Service Requests and File Handling

### Installing PyPi packages using pip

Beyond the packages that come pre-installed, you can also intall packages of choice from thousands of packages available on Python Package Index (PyPi). Run the following command from terminal:

```pip install requests```

Here we are installing `requests` module which is the most popular Python library for interacting with web services.

#### Simple GET Request

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

### Exercise
Code should be implemented in `ex07.py`.

Send a GET request to the url `https://jsonplaceholder.typicode.com/posts`. From the response, print the title of the first 10 post records.

#### Hands-On: Reading/Writing Delimited Files

1. project_utils
2. file_utils
3. data_utils - string and zipping

Send a GET request to the url 'https://jsonplaceholder.typicode.com/users'. From the response remove the 'address' and 'company' attributes of each user. Write the data for the first 10 users in a CSV file. Read the data from this generated CSV file and create list of user objects, where each user object is a dictionary.

For this, hands-on, we'll use various new Python constructs which have been included here for your reference.

Following are basic file reading related Python calls:

```python
f = open("<file_path>", "r") # Opens the file and returns a file object
f.read() # Reads all the content
f.readline() # Reads one line
f.readlines() # Returns an object which can be iterated over to get all lines
f.close() # closes the file handle
```

Following calls can be used to create and write to a file:
```python
f = open("<file_path>", "w") # Opens the file and returns a file object
f.write("<string>") # Write a string
f.writelines("<seq of lines>") # Iterates over the sequence and writes line by line
f.close() # closes the file handle
```

For automatically closing a file when the job is done, you can also use the `with` block:

```python
with <open_command> as <file_object>:
  # operate on the file
```

While handling CSV files (reading/writing), following string methods come handy:
```python
"a,b,c".split(",") . # Can use any delimiter
",".join(['a', 'b', 'c'])
```

Some other built-in Python functions are interest are `dict` and `zip`:
```python
zip([1,2], [3,4]) # returns ((1,3),(2,4))
dict((1,3),(2,4)) # returns {1:3, 2:4}
```

We will make use of various facilities of os module:
```python
import os
os.linesep # for cross-platform line separator
os.path.dirname # to extract directory part from a file path
os.path.realpath # to handle relative path extracted in combination with __file__ magic attribute
os.path.join  # to create a full path from parts by using a cross-platform path separator
```

#### Long Exercise: Reading/Writing Delimited and JSON Files

#### Demo: Reading/Writing XML Files

#### Demo: Simple SOAP POST Request

### 3. Handling Child Processes

#### Hands-On Parent in Blocking Mode using subprocess

#### Demo:  Parent in Non-Blocking Mode using pexpect

#### Long Exercise - Automating Chrome using requests, JSON Wire Protocol and chromedriver

#### Walk-through of a Sample Solution

### 4. Foundations of Selenium WebDriver

#### Automation using JSON Wire Protocol and Requests

#### Hands-On: Basic Raw Scripting using Python Selenium Bindings

#### Python unittest - Test Class, Test Methods, Fixtures and Assertions

#### Long Exercise: Use unittest to implement valid and invalid login scenario.

#### Walk-through of a Sample Solution
