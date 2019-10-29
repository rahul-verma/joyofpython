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


def is_int(in_expr):
    return type(in_expr) is int


def calc_grade(in_expr):
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

    # Loop variant 1
    for number in numbers:
        print(calc_grade(number))

    # Loop variant 2
    for index in range(len(numbers)):
        print(calc_grade(numbers[index]))

    # Loop variant 3
    for index, number in enumerate(numbers):
        print("Index: {}".format(index), calc_grade(number))


def calc_grade_for_console_input():
    number = input("Enter a number:")
    print("Grade is {}".format(calc_grade(int(number))))


def calc_grades_for_console_input_stage1():
    while True:
        number = input("Enter a number (X to quit):")
        if number.strip().lower() == 'x':
            break

        print("Grade is {}".format(calc_grade(int(number))))


def calc_grades_for_console_input():
    while True:
        number = input("Enter a number (X to quit):")
        if number.strip().lower() == 'x':
            break

        try:
            grade = calc_grade(int(number))
        except ValueError:
            print("Not a number")
            continue
        else:
            print("Grade is {}".format(grade))
        finally:
            print("Get ready for next entry")








