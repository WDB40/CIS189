"""
Program: basic_list.py
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Manipulate lists with python
"""


def get_input():
    INVALID_INPUT = -1
    user_input = INVALID_INPUT

    while user_input == INVALID_INPUT:
        user_input = input("Enter a integer value: ")

        try:
            user_input = int(user_input)
        except ValueError:
            user_input = INVALID_INPUT

    return user_input


def make_list():
    value_list = []

    for i in range(0, 3):
        value_list.insert(i, get_input())

    return value_list


if __name__ == '__main__':
    get_input()
