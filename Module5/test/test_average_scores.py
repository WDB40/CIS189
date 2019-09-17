import unittest

from Module5.src.average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average_2_list(self):
        self.assertEqual(25, average([20, 30]))

    def test_average_3_list(self):
        self.assertEqual(25, average([20, 25, 30]))

    def test_average_4_list(self):
        self.assertEqual(30, average([20, 25, 35, 40]))

    def test_average_5_list(self):
        self.assertEqual(25, average([15, 20, 25, 30, 35]))


if __name__ == '__main__':
    unittest.main()
