import unittest

from Module4.src.calculate_order import calculate_shipping, calculate_tax, add_discounts, calculate_order


class MyTestCase(unittest.TestCase):
    def test_under_10_shipping(self):
        self.assertEqual(5.95, calculate_shipping(5))

    def test_10_up_to_30_shipping(self):
        self.assertEqual(7.95, calculate_shipping(10))

    def test_between_10_30_shipping(self):
        self.assertEqual(7.95, calculate_shipping(20))

    def test_30_up_to_50_shipping(self):
        self.assertEqual(11.95, calculate_shipping(30))

    def test_between_30_50_shipping(self):
        self.assertEqual(11.95, calculate_shipping(40))

    def test_50_over_shipping(self):
        self.assertEqual(0, calculate_shipping(50))

    def test_invalid_shipping(self):
        self.assertEqual(-1, calculate_shipping(-50))

    def test_tax_5(self):
        self.assertAlmostEqual(0.3, calculate_tax(5))

    def test_tax_15(self):
        self.assertAlmostEqual(0.9, calculate_tax(15))

    def test_tax_30(self):
        self.assertAlmostEqual(1.8, calculate_tax(30))

    def test_tax_45(self):
        self.assertAlmostEqual(2.7, calculate_tax(45))

    def test_tax_60(self):
        self.assertAlmostEqual(3.6, calculate_tax(60))

    def test_with_only_cash_coupon(self):
        self.assertEqual(add_discounts(10, 5, 0), 5)

    def test_with_only_percent_coupon(self):
        self.assertEqual(add_discounts(10, 0, 0.1), 9)

    def test_with_both_coupons(self):
        self.assertEqual(add_discounts(15, 5, 0.2), 8)

    def test_total_order_1(self):
        self.assertAlmostEqual(36.57, calculate_order(33, 3, 0.1))

    def test_total_order_2(self):
        self.assertAlmostEqual(84.8, calculate_order(105, 5, 0.2))

    def test_total_order_3(self):
        self.assertAlmostEqual(14.006, calculate_order(9, 1, 0.05))


if __name__ == '__main__':
    unittest.main()
