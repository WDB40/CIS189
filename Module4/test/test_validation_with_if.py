import unittest
from Module4.src.validation_with_if import average


class MyTestCase(unittest.TestCase):

    def test_average(self):
        self.assertEqual(90, average(85, 90, 95))

    def test_average_again(self):
        self.assertEqual(77, average(77, 77, 77))


if __name__ == '__main__':
    unittest.main()
