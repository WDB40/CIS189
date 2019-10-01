"""
Program: test_inner_functions.py (inner_functions_assignment.py)
Author: Wes Brown
Last date modified: 10/01/19

Purpose: Test working with inner functions.
"""


import unittest
from Module6.src.inner_functions_assignment import measurements


class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(measurements([2.1, 3.4]), "Perimeter = 11.00 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(measurements(3.5), "Perimeter = 14.00 Area = 12.25")


if __name__ == '__main__':
    unittest.main()
