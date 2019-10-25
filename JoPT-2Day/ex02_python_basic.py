
def print_value(in_expr):
    print(in_expr)


# you can return an object
def get_type(in_expr):
    return type(in_expr)


# You can chain calls
def print_type(in_expr):
    print(type(in_expr))  # You can use your own defined functions above as well.


# Type checking
def is_int(in_expr):
    return type(in_expr) is int


# Type conversion
def convert_to_int(in_expr):
    return int(in_expr)


# Return grade <= 40: C, >40 <=80 B, >80 A
def calc_grade(in_expr):
    if in_expr <= 40:
        return "C"
    elif in_expr <= 80:
        return "B"
    else:
        return "A"


#Improved
def calc_grade_2(in_expr):
    if not is_int(in_expr):
        raise Exception("Not an int")

    if in_expr <= 40:
        return "C"
    elif in_expr <= 80:
        return "B"
    else:
        return "A"


# For a series of numbers
def calc_grades(numbers):
    for number in numbers:
        print(calc_grade_2(number))

    for index in range(len(numbers)):
        print(calc_grade_2(numbers[index]))

    for index, number in enumerate(numbers):
        print("Index: {}".format(index), calc_grade_2(number))


def calc_grade_for_console_input():
    number = input("Enter a number:")
    number = convert_to_int(number)
    print("Grade is {}".format(calc_grade(number)))


def calc_grades_for_console_input():
    while True:
        number = input("Enter a number (X to quit):")
        if number.strip().lower() == 'x':
            break

        number = convert_to_int(number)
        print("Grade is {}".format(calc_grade(number)))


def calc_grades_for_console_input_2():
    while True:
        number = input("Enter a number (X to quit):")
        if number.strip().lower() == 'x':
            break

        try:
            number = convert_to_int(number)
        except ValueError:
            print("Not a number")
            continue
        else:
            print("Grade is {}".format(calc_grade(number)))
        finally:
            print("Get ready for next entry")


# Importing a module
import math


def calc_sqrt(in_num):
    if type(in_num) is not int or type(in_num) is not float:
        raise Exception("Not a number")
    return math.sqrt(in_num)


# You can make a python import anywhere, even within a function
# Handle sqrt of negative numbers
def calc_sqrt_2(in_num):
    import math, cmath
    if type(in_num) is not int and type(in_num) is not float:
        raise Exception("Not a number")

    if in_num >= 0:
        return math.sqrt(in_num)
    else:
        return cmath.sqrt(in_num)

# print(calc_sqrt_2(0))
# print(calc_sqrt_2(4))
# print(calc_sqrt_2(4.6))
# print(calc_sqrt_2(-4.6))


# For those who are interested
# In Python conditional imports are possible along with aliases
def calc_sqrt_3(in_num):
    if type(in_num) is not int and type(in_num) is not float:
        raise Exception("Not a number")

    if in_num >= 0:
        import math as math_mod
    else:
        import cmath as math_mod

    return math_mod.sqrt(in_num)


print(calc_sqrt_3(0))
print(calc_sqrt_3(4))
print(calc_sqrt_3(4.6))
print(calc_sqrt_3(-4.6))







