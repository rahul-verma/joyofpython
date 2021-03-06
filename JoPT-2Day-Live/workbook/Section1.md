## 1. Python Fundamentals

- [Fundamental Python Constructs](#fundamental-python-constructs)
- [Importing modules](#importing-modules)
- [Creating Python Project and Running Our First Script](#creating-python-project-and-running-our-first-script)
- [Creating Basic Functions](#creating-basic-functions)
- [Conditional Control Structures](#conditional-control-structures)
- [Exercise](#exercise)
- [Exercise: Creating a Package and Module](#exercise-creating-a-package-and-module)
- [Raising an Exception](#raising-an-exception)
- [Exercise](#exercise-1)
- [for Loop](#for-loop)
- [Exercise](#exercise-2)
- [Taking Input from Console](#taking-input-from-console)
- [Exercise](#exercise-3)
- [`while` Loop](#while-loop)
- [Exercise](#exercise-4)
- [Exception Handling](#exception-handling)
- [Exercise](#exercise-5)
- [Long Exercise: The MindMaster Game](#long-exercise-the-mindmaster-game)
  * [Business Requirements](#business-requirements)
  * [Tips and Inputs](#tips-and-inputs)
- [Walk-through: A Sample Solution](#walk-through-a-sample-solution)

### Fundamental Python Constructs

We are going to use Python Interactive Shell for this section.

Python is an object-oriented, dynamically-typed, interpreted language. 

Python can as well be used for procedural-style, object-based language unless you write types/classes of your own. This workshop mostly covers this style of programming, given the 2-day time window. Also, most testers use Python in this format before maturing to the object-oriented style of Python usage. In the last section, we would briefly touch upon this as well.

Type of a variable (referred to as a `name` in Python) is essentially the type of object it points to.

```python
>>>a = 1
>>>f = 1.1
>>>b = True
```

Names in Python mostyl follow these rules (for variables, functions/methods, modules, packages - i.e. most of the names):
  - Contain letters, numbers and underscore `_`
  - Can not start with a number
  - All letters in lower case (except global vars, constants etc where all uppercase letters are used.)
  - Multiple words separated by an underscore `_`
  - Underscore(s) at the beginning of the name has special meaning. More on this later.

As the left hand side in the assignment is just a name without a type of its own, it can be assigned to an object of another type. Remember that this, in general, is not suggested. There are specific situations where it comes handy, which we would cover in the workshop.

```python
>>>b = 1
```

You don't need to worry about size of numbers in Python.
```python
>>>a = 11111111111236723546735467235476235467523475234675236745237452376452376452374527354573
```

Python provides 2 types of sequential containers.

First one is a `list` which is a variable size container i.e. you can add any number of elements based on need.
```python
>>>l = [1, 2, 3]
```

Second seqquence type is `tuple`.
```python
>>>t = (1, 2, 3)
```

Sequences support index-based retrieval of items. Index follows computer counting (starts from 0).
```python
>>>l[0]
>>>t[0]
```

Lists are mutable. Tuples are immutable. Here the second statement will throw an exception.
```python
>>>l[0] = 5
>>>t[0] = 5
```

Strings can be defined in Python using single or double quotes. There is another category of strings with triple quotes, which we will see later.

```python
>>>s = "testing"
>>>s = 'testing'
```

Strings are sequences too. Each character is an item.
```python
>>>s[0]
```

Strings are immutable. This statement will throw an exception.
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

Python has a built-in `set` type as well. A fundamental property of a set is that it contains unique items.
```python
>>>s1 = {1,2,3}
```

As both dictionary and set use curly braces `{}` as markup, to declare an empty set you need a `set()` call.
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
>>>3**2
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
>>>a == 1  # returns True
```

For containers, the behavior is based on other factors. For example for sequences, each element is compared in order. Size comes next.
```python
>>>[10,3] > [2,3,4,5,6,7]
>>>[2,3] > [2,3,4,5,6,7]
```

As discussed earlier, Python support both procedural and object-oriented styles of programming.

Many built-in functions as well as classes/types are available without any imports when the Python Interpreter loads.

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

There is a special keyword `is` which can be used for relational operation. It checks whether two objects are same.

Here we are using it for type checking.
```python
>>>type(1) is int
```

You can also convert an object to another object type if it is allowed. Here, the last conversion will raise an exception.
```python
str(1)
int("1")
int("test")
```

Everything is an object in Python - a concept which is at the heart of the language. The simple objects we created so far offer behaviors. These behaviors are just like functions but attached to a particular object's state. You can call a method by using the method resolution operator - `.` (dot).

Here, we are calling the `append` method of a list object to add another element to the list.
```python
>>>l1 = [4,3,5]
>>>l1.append(1)
>>>l1
```

### Importing modules
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

### Creating Python Project and Running Our First Script
We are using PyCharm as the default IDE here, but you can use a Python IDE that you are comfortable with.

Let's get started:
  - Create Python Project
  - Copy all the contents of this directory from GitHub repository to the root directory of the project.
  
**Note: The skeletons/placeholders for all scripts that we are going to implement are present in the `scripts` directory.**

In the `ex01.py` script, add the following:

```python
print("The Joy of Python")
```

We can run the script using the IDE or from the terminal by running the command: `python ex01.py`.

### Creating Basic Functions

Functions in Python are defined using the keyword `def`.

```python
def function_name(arg1, arg2):
  # Function body
  return object1
```

The critical part to notice is that Python marks **blocks using indentation** unlike curly braces or begin & end markers in other languages. In other languages, it is suggested that you indent a child block for readability. Python in this matter imposes it on you and the code does not run without proper indentation. Depending on your school of thought, you might like or disklike this.

You can indent using a tab or a fixed number of spaces. As per PEP8 you should use 4 spaces for indentation.

A function can take 0 or more arguments. The names 'arg1', 'arg2' etc are available as names (local scope) within the function body. The function can return one or more objects. If no return statement is supplied, then it returns `None` (which is eqivalent of `NULL/null` in other languages)

Once defined, you can call this function just like built-in functions.
```python
ret_val = function_name(1, 'testing')
```

### Conditional Control Structures

Python supports code blocks that get executed when a condition is True or False.

It uses the familiar `if` and `else` keywords.

For chaining of conditions, i.e. the `else if` situation, rather than two separate keywords, Python has a special keyword - `elif`.

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

### Exercise
In the script `ex01.py`, create a function with name `calc_grade` which takes a score (integer) as an argument and returns grade as string as per the following rules:
  - 'C' grade if score <= 40
  - 'B' grade if 40 < score <= 80
  - 'A' grade if 80 < score

 Call the function and experiment.

### Exercise: Creating a Package and Module
Multiple modules can reside inside a single `package`. A `package` is a directory/folder containing an `__init__.py` file. (In Python 3.3+ concept of namespace packages that don't need `__init__.py` was introduced. Beyond scope of this workshop). You can do a lot of advanced stuff in `__init__.py`. For this workshop, a blank file suffices.

In the project, you can see that there is a `jopt` package already created. In this package, various modules are present. One of them is `basics.py` which contains skeletons of various functions that you are going to implement one by one.

  - Copy the contents of `calc_grade` function that you have created in `ex01.py` to corresponding function in `basics.py`
  - In the `ex02.py` file, add the following contents and execute:

```python
from jopt.basics import *
grade = calc_grade(43)
print(grade)
```

### Raising an Exception

Rather than returning an error code, in Python you usually raise/throw an exception object.

You can raise an exception in Python by creating an exception object. Python does not use the `new` keyword like other languages, so creation of an object looks like a function call.

You can raise an exception using the `raise` keyword.

```python
raise Exception("This didn't go well")
```

### Exercise
Improve the `calc_grade` function to throw an exception when a non-int object is provided. Run the `ex02.py` script by providing non-integers to evaluate the behavior.

### `for` Loop

The most commonly used construct in Python is probably the one where you iterate on a container using a `for` loop:

```python
for element in elements:
  print(element)
```

**Tip:** Name a list with a plural name. It goes a long way in the readability of your `for` loops on lists.

Python's built-in function `range(limit)` generates numbers from 0 till `limit-1`. Hence it is a good way to generate indices, especially when you are iterating over a list:

```python
for index in range(len(elements)):
  print(elements[index])
```

There is an obvious negative impact on readability with the above approach. One can use `enumerate()` call instead, as follows:

```python
for index, element in enumerate(elements):
  print(index, element)
```

### Exercise
Implement the function `calc_grades` in `basics.py`, which takes a list argument. It should implement a for loop which prints grades for all the integers in the list by calling `calc_grade` function.

Call and experiment with the function in `ex03.py`.

### Taking Input from Console

You can take input from console using the built-in `input()` function. Remember that it always returns a string, so you might have to use the type conversion functions before using the value.

Also, make wise use of the prompt argument to provide intuitive prompt messages to user.

```python
age = input("What's your age? ")
print(int(age))
```

### Exercise
Implement the function with name `calc_grade_for_console_input`in `basics.py`, which takes an integer from console as an input and prints its grade.

Call and experiment with the function in `ex04.py`.

### `while` Loop
Another style of loop which can be used in Python is a `while` loop. You use it when the decision to stop the loop is taken within the body of the loop. In short, use it when you don't know how many iterations should be executed before starting the loop.

```python
while condition:
  body with decision about when to exit the loop
```

Here, the loop runs as long as the condition evaluates to True or as a result of a `break` statement.

### Exercise
Implement the function with name `calc_grades_for_console_input` in `basics.py`, which uses `while` loop to take integer as input from console and prints the grade using `calc_grade` function call. The program should exit when user enters 'x' in lower or upper case.

Call and experiment with the function in `ex05.py`.

### Exception Handling
Error handling based code usually relies on preventive checking of potential problems that could take place.

Exception handling on the other hand, usually lets the problem take place and handles it at appropriate layers. This is a common found feature in all OOP languages.

Python supports a 4-block exception handling construct. Out of these, one tends to use only the `try` and `except` blocks most of the times.

```python
try:
  #try this block
except ExceptionName1 as e:
  # do this if exception of type ExceptionName1 was raised
except ExceptionName2 as e:
  # do this if exception of type ExceptionName2 was raised
else:
  # do this if no exception occurred
finally:
  # do this always
```

### Exercise
Modify the function `calc_grades_for_console_input` in `basics.py`, to include exception handling for the case where user enters a non-integer. The goal is to let the program continue in case of invalid input by informing the user that it was invalid.

Call and experiment with the function in `ex05.py`.

### Long Exercise: The MindMaster Game
Create a MindMaster Game in `ex06_mindmaster.py`. You can treat it as the main script and create functions/modules the way you like. One thing to certainly avoid is writing a monolithic script.

#### Business Requirements
1. The Program thinks about a 3-digit number.
2. User is given 10 attempts to guess the number via Console/Terminal.
3. For each guess, user is provided feedback. The feedback mentions 2 pieces of information - how many digits are correct and how many digits are at correct position.
4. User is able to play the game any number of times.
5. After each game play, the program informs the user about how many games s/he won or lost.


#### Tips and Inputs
1. User `format()` for string formatting instead of string concatenation (using `+`). For example: `"test {} {}".format(1, 'testing')` will return `test 1 testing`. The curly braces `{}` are used as placeholders.
2. Use a dictionary for storing number of games won and lost.
3. Handle and process exception for a non-int entry. It would be counted as an attempt.
4. When you convert a string to a list, each character is an item in the list.
5. `strip()` method of string removes the extraneous spaces at head as well as tail.
6. You can generate a random integer between a range by using `randint(x,y)` function in `random` module.

### Walk-through: A Sample Solution
Let's look at the details of a possible solution. Map to the way you approached the problem and take a note of any new learning or a different way of solving the same problem.
