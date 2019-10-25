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

'''
These would be explored in Python Interactive Shell.
Included here for completeness sake.
'''

# Using short variable names as goal is to demonstrate code blocks for learning purpose.
# In any real program, even if exercise code, use proper and useful names.

# Assigning Object to a Name (Variable in other langs)
a = 1  # int
f = 1.1  # float
b = True  # bool

# Same name can be assigned later to any other type of object. Loosely Typed.
# NOT suggested.
b = 1

# Number can be of any length
a = 11111111111236723546735467235476235467523475234675236745237452376452376452374527354573

# Sequences, Support index based retrieval
l = [1, 2, 3]
print(l[0])
t = (1, 2, 3)
print(t[0])
s = "testing"  # Yes, string is a seq of chars
print(s[0])

# Only list as a sequence is mutable
l[0] = 5
print(l)
t[0] = 5  # exception
s[0] = 'r'  # exception


# Dictionary (Mapping type)
d = {1: 2, 3: 4}
print(d[1])  # key based access


# Set - supports set operations - can revisit later.
s1 = {1,2,3}
s2 = set()  # An empty set has to be declared in this manner as {} means empty dict.

# Calling built-in functions
print("Hello")

# Basic operators
print(1+1)  # +, -, *, % are similar to other langs
print(1/3)
print(1//3)  # slashes decimal places
print(3 ** 2)

# Augmented operators
a = 1
a += 1  # same as a = a + 1. Works for other operators.
print(a)

# Relational operators
a = 1
print(a == 1)  # >, <, <=, >=, != are others

# For containers, the bejavior is based on other factors.
# For example for sequences, each element is compared in order. Size comes next.
print([10,3] > [2,3,4,5,6,7])
print([2,3] > [2,3,4,5,6,7])

# Function Call chain, know type of object
print(type(1))

# Type checking (for built-in basic scalars and containers) using 'is' operator
# Try other data types
print(type(1) is int)

# Type conversion
print(str(1))
print(int("1"))
print(int("test"))  # problem

# Calling methods of an object
l1 = [4,3,5]
l1.append(1)
print(l1)

#######################################
# We would cover these using functions
# Included here only for reference.
#######################################

# Conditional Control flow
if 1 == 1:
    print("Of course.")

if 1 != 2:
    print("Not really")
else:
    print("Captain obvious.")


if 1 != 2:
    print("Does not come here.")
elif 2 == 2:
    print("comes here")


# Logical operators
if True and True:
    print("Whole truth")

if True and False:
    print("Lost the game there")

if False or False:
    print("Second one is a winner")

if not False:
    print("I never thought to not help you.")


# Loops - Different flavours of for
tests = ['t1', 't2', 't3']  # Professional Tip: Name list as a plural.

for test in tests:
    print(test)

for index in range(len(tests)):  # Bye bye readability
    print(tests[index])

for index, test in enumerate(tests):  # Welcome back readability
    print(index, test)


# Loops - while

counter = 1
while counter <= 5:
    # A little bit of formatting.
    print("Counting: {}".format(counter))
    counter +=1


# Break and Continue
numbers = range(15)

for number in numbers:
    if number % 2 == 0:
        continue
    elif number == 13:
        print("Scary")
        break
    print(number)

# Writing a basic function

def multiply(left, right):
    return left * right


print(multiply(3,4))


# Writing a basic class, with bound method

class Calculator:

    def multiply(self, left, right):  # self is current obj ref, just like 'this'. Only in def.
        return left * right


calc = Calculator()
print(calc.multiply(3, 4))  # No need to pass self ref while calling a method.


# Writing a class method in a class


class Calculator:

    @classmethod
    def multiply(cls, left, right):
        return left * right


print(Calculator.multiply(3, 4))


# Importing modules
import math
print(math.sqrt(4))
from math import sqrt
print(sqrt(9))


# Basic exception handling

try:
    a = int("testing")
except Exception as e:
    print(e)
    import traceback  # Yes, you can import a module anywhere.
    traceback.print_exc()
else:
    pass  # Code block in case of no exception
finally:
    pass  # Code block irrespective of exception or not.


# Exercise
#Style 1

def square_it(in_list):
    out_list = []
    for i in in_list:
        out_list.append(i ** 2)
    return out_list


print(square_it(range(5)))


# Style 2 - List comprehension
print([i**2 for i in range(5)])



