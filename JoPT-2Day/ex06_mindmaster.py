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


import random
import signal
import sys
import os

history = {
    "won": 0,
    "lost": 0
}

confirmation = 'y'


def convert_number_to_str_digit_list(in_num):
    return list(str(in_num))


def calc_right_positions(left, right):
    right_positions = 0
    for index, value in enumerate(left):
        if right[index] == value:
            right_positions += 1
    return right_positions


def calc_num_right_digits(left, right):
    for digit in left:
        try:
            right.remove(digit)
        except:
            pass

    return len(left) - len(right)


def provide_feedback(processed_left, right):
    processed_right = convert_number_to_str_digit_list(right)
    right_positions = calc_right_positions(processed_left, processed_right)
    right_digits = calc_num_right_digits(processed_left, processed_right)
    print(
        "Your guess has {} right digit(s), with {} digit(s) at correct position.".format(right_digits, right_positions))


def generate_random_int(start, end):
    return random.randint(start, end)


def is_empty(in_data):
    return len(in_data) == 0


def is_within_limits(in_data, start, end):
    return in_data >= start or in_data <= end


def start_single_game(start=101, end=999, max_allowed_attempts=10):
    print('''

    I've thought of a 3 digit number.
    For each guess that you make, I'd give you feedback.
    Note the feedback and pattern to guess the number.

    Let's play. All the best!

    ''')

    number_thought = generate_random_int(start, end)
    processed_thought = convert_number_to_str_digit_list(number_thought)
    current_attempt = 0

    while current_attempt < max_allowed_attempts:
        current_attempt += 1
        attempt = input("What's your guess? ").strip()

        if is_empty(attempt):
            print("You think I guessed an empty int :-)?. Try again.")
            continue

        try:
            attempted_int = int(attempt)
        except:
            print("Your guess is not an integer. Try again.")
            continue
        else:
            if not is_within_limits(attempted_int, start, end):
                print("Your guess is out of my thinking range ({}-{}). Try again.".format(start, end))
                continue
            elif attempted_int == number_thought:
                print("Hurray! You guessed it right in {} attempts. We think alike.".format(current_attempt))
                history["won"] += 1
                return
            else:
                provide_feedback(processed_thought, attempted_int)

    print("Sorry. You exhausted all your attempts. The number was: ", number_thought)
    history["lost"] += 1


def sig_handler(sig, frame):
    print("Goodbye!")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, sig_handler)

    print(os.linesep + "Hello and Welcome to MindMaster!")
    global confirmation

    while confirmation == 'y':
        start_single_game()
        print("Player Stats: Won: {}. Lost: {}".format(history["won"], history["lost"]))
        restart = input("Play again?[y/n] ")
        confirmation = restart[0].lower()

    print("Thanks for playing.")


main()
