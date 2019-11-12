"""
Program: Bicycle.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Using the Rider abstract class
"""


from Module12.src.Rider import Rider


class Bicycle(Rider):
    def ride(self):
        return "Human powered, not enclosed"

    def rider(self):
        return "1 or 2 if tandem or a daredevil"
