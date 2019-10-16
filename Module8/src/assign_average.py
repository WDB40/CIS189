"""
Program: assign_average.py
Author: Wes Brown
Last date modified: 10/15/19

Purpose: Using dictionaries to implement a switch-esque statement
"""


def switch_average(key):
    KEY_NOT_FOUND = -1

    key.upper()

    switcher = {
        "A": 90,
        "B": 80,
        "C": 70,
        "D": 60,
        "F": 50
    }

    return switcher.get(key, KEY_NOT_FOUND)
