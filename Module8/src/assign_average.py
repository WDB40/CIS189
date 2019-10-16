"""
Program: assign_average.py
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Using dictionaries to implement a switch-esque statement
"""


def get_a():
    return 90


def get_b():
    return 80


def get_c():
    return 70


def get_d():
    return 60


def get_f():
    return 50


def switch_average(key):
    KEY_NOT_FOUND = -1

    switcher = {
        "A": get_a(),
        "B": get_b(),
        "C": get_c(),
        "D": get_d(),
        "F": get_f()
    }

    func = switcher.get(key.upper(), KEY_NOT_FOUND)

    return func
