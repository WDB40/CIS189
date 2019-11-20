"""
Program: test_number_guesser.py
Author: Wes Brown
Last date modified: 11/19/19

Purpose: Testing the number guesser class
"""

import unittest
from Module13.src.number_guesser import NumberGuesser


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.number_guesser = NumberGuesser()

    def tearDown(self):
        del self.number_guesser

    def test_add_value(self):
        value = 7
        self.number_guesser.add_guess(value)

        if value not in self.number_guesser.guessed_list:
            self.fail("Value not added to guessed list.")


if __name__ == '__main__':
    unittest.main()
