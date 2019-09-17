import unittest

from Module4.src.calculate_order import calculate_shipping, calculate_tax


class MyTestCase(unittest.TestCase):
    def test_under_10_shipping(self):
        self.assertEqual(calculate_shipping(5), 5.95)

    def test_10_up_to_30_shipping(self):
        self.assertEqual(calculate_shipping(10), 7.95)

    def test_between_10_30_shipping(self):
        self.assertEqual(calculate_shipping(20), 7.95)

    def test_30_up_to_50_shipping(self):
        self.assertEqual(calculate_shipping(30), 11.95)

    def test_between_30_50_shipping(self):
        self.assertEqual(calculate_shipping(40), 11.95)

    def test_50_over_shipping(self):
        self.assertEqual(calculate_shipping(50), 0)

    def test_invalid_shipping(self):
        self.assertEqual(calculate_shipping(-50), -1)

    def test_tax_5(self):
        self.assertEqual(calculate_tax(5), 0.3)

    def test_tax_15(self):
        self.assertEqual(calculate_tax(15), 0.9)

    def test_tax_30(self):
        self.assertEqual(calculate_tax(30), 1.8)

    def test_tax_45(self):
        self.assertEqual(calculate_tax(45), 2.7)

    def test_tax_60(self):
        self.assertEqual(calculate_tax(60), 3.6)

    def test_with_only_cash_coupon(self):
        pass

    def test_with_only_percent_coupon(self):
        pass

    def test_with_both_coupons(self):
        pass

    def test_total_order_1(self):
        pass

    def test_total_order_2(self):
        pass

    def test_total_order_3(self):
        pass


if __name__ == '__main__':
    unittest.main()
