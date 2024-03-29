"""
Program: test.py (average_score.py)
Author: Wes Brown
Last date modified: 09/09/19

Purpose: To create, test, and use an average function.
"""

import unittest
from unittest import mock

from Module3.src.average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert average() == 90

    def test_average_again(self):
        with mock.patch('builtins.input', side_effect=[77, 77, 77]):
            assert average() == 77


if __name__ == '__main__':
    unittest.main()
