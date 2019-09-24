"""
Program: input_while_exit.py
Author: Wes Brown
Last date modified: 09/23/19

Purpose: To take in values and then print them out.
"""


def get_list_of_numbers():
    MIN = 1
    MAX = 100
    STOP = -1
    user_input = 0
    numbers = []

    while user_input != STOP:
        user_input = float(input("Enter a value between 1 and 100 (or -1 to exit): "))

        if user_input == STOP:
            break

        if MIN <= user_input <= MAX:
            numbers.append(user_input)

    return numbers


def print_list(input_list):
    for item in input_list:
        print(item)


if __name__ == '__main__':
    print_list(get_list_of_numbers())

# Not entirely sure what is meant by the assignment, but I think it wants the same functionality as before, but with a break instead
# I added the break and tested the same kind of scenarios as the previous version
# This includes numbers above and below the range specified
# It does not include tests for for non-numeric since that wasn't a requirement (could add similar to the previous assignment)
# If they do enter the -1, they exit the entire way out (which is what I believe is the right behavior)
