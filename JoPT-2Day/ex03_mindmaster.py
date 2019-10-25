'''

Create a MindMaster Game.

Business Requirements
1. The Program thinks about a 3-digit number.
2. User is given 10 attempts to guess the number via Console/Terminal.
3. For each guess, user is provided feedback. The feedback mentions 2 things - how many digits are correct and how many digits are at correct position.
4. User is able to play the game any number of times.
5. After each game play, the program informs the user about how many games s/he won or lost.


Technical Requirements
1. Whether the number contains duplicate digits should be configurable.
2. User .format() for string formatting instead of string concatenation using +.
3. Use a dictionary for storing number of games won and lost.
4. Handle and process exception for a non-int entry. It would be counted as an attempt.

Hints
1. You can use built-in input() function to take user input from terminal:

x = input("prompt")

Make the prompt useful for the user to understand.

2. When you convert a string to a list, each character is an item in the list.

3. .strip() method of string removes the extraneous spaces at head as well as tail.

4. You can generate a random integer between a range by using randint(x,y) function in random module.
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
    print("Your guess has {} right digit(s), with {} digit(s) at correct position.".format(right_digits, right_positions))


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
