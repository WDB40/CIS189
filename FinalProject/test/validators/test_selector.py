import unittest
from FinalProject.src.validators.selector import Selector


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.selector = Selector()

    def test_valid_selector(self):
        self.selector.profit = True
        self.selector.debt_equity = True
        self.selector.roa = True
        self.selector.income = True
        self.selector.volume = True

        self.assertTrue(self.selector.validate_state())

    def test_invalid_selector_below_five(self):
        self.selector.profit = True
        self.selector.debt_equity = True
        self.selector.roa = True
        self.selector.income = True

        self.assertFalse(self.selector.validate_state())

    def test_invalid_selector_above_five(self):
        self.selector.profit = True
        self.selector.debt_equity = True
        self.selector.roa = True
        self.selector.income = True
        self.selector.volume = True
        self.selector.market_cap = True

        self.assertFalse(self.selector.validate_state())


if __name__ == '__main__':
    unittest.main()
