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
