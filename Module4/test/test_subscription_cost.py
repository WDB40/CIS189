"""
Program: test_subscription_cost.py (subscription_cost.py)
Author: Wes Brown
Last date modified: 09/10/19

Purpose: Test the code that receives a subscription level and print the cost.
"""


import unittest
from unittest import mock

from Module4.src.subscription_cost import print_subscription_cost


class MyTestCase(unittest.TestCase):
    def test_platinum(self):
        with mock.patch('builtins.input', side_effect=["Platinum"]):
            assert print_subscription_cost() == 60

    def test_gold(self):
        with mock.patch('builtins.input', side_effect=["Gold"]):
            assert print_subscription_cost() == 50

    def test_silver(self):
        with mock.patch('builtins.input', side_effect=["Silver"]):
            assert print_subscription_cost() == 40

    def test_bronze(self):
        with mock.patch('builtins.input', side_effect=["Bronze"]):
            assert print_subscription_cost() == 30

    def test_free(self):
        with mock.patch('builtins.input', side_effect=["Free"]):
            assert print_subscription_cost() == 0

    def test_platinum_lower(self):
        with mock.patch('builtins.input', side_effect=["platinum"]):
            assert print_subscription_cost() == 60

    def test_gold_lower(self):
        with mock.patch('builtins.input', side_effect=["gold"]):
            assert print_subscription_cost() == 50

    def test_silver_lower(self):
        with mock.patch('builtins.input', side_effect=["silver"]):
            assert print_subscription_cost() == 40

    def test_bronze_lower(self):
        with mock.patch('builtins.input', side_effect=["bronze"]):
            assert print_subscription_cost() == 30

    def test_free_lower(self):
        with mock.patch('builtins.input', side_effect=["free"]):
            assert print_subscription_cost() == 0


if __name__ == '__main__':
    unittest.main()
