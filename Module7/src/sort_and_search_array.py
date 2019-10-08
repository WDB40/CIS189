"""
Program: sort_and_search_array.py
Author: Wes Brown
Last date modified: 10/07/19

Purpose: Sorting and searching an array in python.
"""


import array as arr


def sort_array(items):
    # from a testability perspective, I am going to return a value
    items_array = arr.array('i', items)
    back_to_list = items_array.tolist()
    back_to_list.sort()
    items_array = arr.array('i', back_to_list)
    return items_array


def search_array(items, item):
    items_array = arr.array('i', items)
    INVALID_VALUE = -1
    index = INVALID_VALUE

    try:
        index = items_array.index(item)
    except ValueError:
        index = INVALID_VALUE

    return index


if __name__ == '__main__':
    pass
