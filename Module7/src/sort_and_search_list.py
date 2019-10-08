"""
Program: sort_and_search_list.py
Author: Wes Brown
Last date modified: 10/07/19

Purpose: Sorting and searching a list in python.
"""


def sort_list(items):
    # we aren't passing anything back since the reference is based in
    pass


def search_list(items, value):
    INVALID_VALUE = -1
    index = INVALID_VALUE

    try:
        index = items.index(value)
    except ValueError:
        index = INVALID_VALUE

    return index


if __name__ == '__main__':
    pass
