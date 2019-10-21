"""
Program: dictionary_ops.py
Author: Wes Brown
Last date modified: 10/20/19

Purpose: Contains a function for printing a dictionary
"""


def print_dict(the_dict):
    for key, value in the_dict.items():
        print(key, value)
