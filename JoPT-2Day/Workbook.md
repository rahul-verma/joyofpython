## The Joy of Python for Testers - Workbook for 2-day version

### 1. Python Fundamentals

#### Fundamental Python Constructs

Python is losely typed language. Type of a variable (referred to as a name) is essentially the type of object it points to.

```python
>>>a = 1
>>>f = 1.1
>>>b = True
```

As the left hand side in the assignment is just a name without a type of its own, it can be assigned to an object of another type. Remember that this is, in general, not suggested. There are specific situations where it comes handy, which we would cover in the workshop.

```python
>>>b = 1
```

You don't need to worry about size of numbers in Python.
```python
>>>a = 11111111111236723546735467235476235467523475234675236745237452376452376452374527354573
```

Python provides 2 types of sequential containers.

First one is a list which is a variable size container, without you worrying about the size.
```python
>>>l = [1, 2, 3]
```

Second seqquence type is tuple.
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

Python has a built-in mapping data type called dictionary. 
```python
>>>d = {1: 2, 3: 4}
```

You can retrieve an item from a dictionary by using corresponding key. Syntax is similar to sequence's index based retrieval.
```python
>>>d[1]
```

Python has a built-in set type as well.
```python
>>>s1 = {1,2,3}
```

As both dictionary and set use curly braces {}, as markup, to declare an empty set you need a set() call.
```python
>>>s2 = set()
```

Python supports the usual operators like other languages +, -, *, %
```python
>>>1+1
```

Python has 2 different division operators for cater to 2 different needs.
```python
>>>1/3
>>>1//3
```

Python uses ** as the exponentiation (power) operator.
```python
>>>3 ** 2
```

Python supports augmented operators. E.g. instead of a = a+1, you can do the following:
```python
>>>a = 1
>>>a += 1
>>>a
```

Python supports familiar relational operators to compare basic types: ==,>, <, <=, >=, != 
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

You can check type of an object.
You can chain function calls.
```python
>>>type(1)
```

You can chain function calls.
```python
>>>print(type(1))
```

There is a special keyword 'is' which can be used for relational operation is well. More on this later.

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

Everything is an object in Python - a concept which is at the heart of the language. The simple objects we created so far offer behaviors. These behaviors are just like functions but attached to a particular object's state. You can call a method by using the method resolution operator that is a '.' (dot).

Here, we are calling the 'append' method of a list object to add another element to the list.
```python
>>>l1 = [4,3,5]
>>>l1.append(1)
>>>l1
```

#### Creating Basic Functions

#### Conditional Control Structures

#### Exception Raising and Handling

#### Loops

#### Taking Input from Console

### 2. Basic Web Service Requests and File Handling

#### Simple GET Request

#### Reading/Writing Delimited Files

#### Reading/Writing JSON Files

#### Reading/Writing XML Files

#### Simple SOAP POST Request

### 3. Handling Child Processes

#### Parent in Blocking Mode using subprocess

#### Parent in Non-Blocking Mode using pexpect

### 4. Basics of Python unittest

### Understanding Test Class, Test Methods, Fixtures and Assertions

### 5. Foundations of Selenium WebDriver

#### Automation using JSON Wire Protocol and Requests

#### Basic Raw Scripting using Python Selenium Bindings

#### Steps towards a basic framework structure




