"""
Program: Car.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Using the Rider abstract class
"""


from Module12.src.Rider import Rider


class Car(Rider):
    def ride(self):
        return "Engine powered, enclosed"

    def rider(self):
        return "1 plus comfortably"
