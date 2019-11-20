"""
Program: number_guesser.py
Author: Wes Brown
Last date modified: 11/19/19

Purpose: Contain information related to the guessed values in a number guessing game
"""


class NumberGuesser:
    def __init__(self, guessed_list=None):
        self.guessed_list = guessed_list

    @property
    def guessed_list(self):
        return self._guessed_list

    @guessed_list.setter
    def guessed_list(self, value):
        self._guessed_list = value

    def add_guess(self, value):
        self._guessed_list.append(value)
