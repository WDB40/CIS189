"""
Program: Shape.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Abstract class to test
"""


from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        raise NotImplementedError("Abstract method not implemented")
