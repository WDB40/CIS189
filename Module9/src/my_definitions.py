"""
Program: my_definitions.py
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Creates a file with a few functions
"""


def greeting():
    print("Howdy there.")


def message():
    print("Author: Wes Brown")


def print_dict(the_dict):
    for key, value in the_dict.items():
        print(key, value)


def print_set(the_set):
    for item in the_set:
        print(item)


if __name__ == '__main__':
    pass
