import unittest

from Module5.src.average_scores import average


class MyTestCase(unittest.TestCase):
    def test_average_2_list(self):
        self.assertEqual(25, average([20, 30]))


if __name__ == '__main__':
    unittest.main()
