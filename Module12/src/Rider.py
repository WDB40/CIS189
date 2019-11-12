"""
Program: Rider.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Abstract class to be used by others
"""


from abc import abstractmethod


class Rider:
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def rider(self):
        pass
