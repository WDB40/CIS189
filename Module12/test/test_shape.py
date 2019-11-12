"""
Program: test_shape.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Testing what happens when the abstract method is called
"""


import unittest

from Module12.src.Shape import Shape


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.shape = Shape()

    def tearDown(self):
        del self.shape

    def test_abstract_method(self):
        with self.assertRaises(NotImplementedError):
            self.shape.area()


if __name__ == '__main__':
    unittest.main()
