import unittest


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(5 == 5)

    def test_not_equal(self):
        self.assertTrue(5 != 10)

    def test_greater_than(self):
        self.assertTrue(10 > 5)

    def test_less_than(self):
        self.assertTrue(5 < 10)

    def test_greater_than_equal(self):
        self.assertTrue(10 >= 5)

    def test_less_than_equal(self):
        self.assertTrue(5 <= 10)

    def test_equal_two(self):
        self.assertFalse(5 == 10)


if __name__ == '__main__':
    unittest.main()
