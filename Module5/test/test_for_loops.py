import unittest

from Module5.src.for_loops import average


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(5, average(4, 5, 6))


if __name__ == '__main__':
    unittest.main()
