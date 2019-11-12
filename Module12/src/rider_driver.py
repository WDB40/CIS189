"""
Program: Bicycle.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Using the Rider abstract class and derived class
"""


from Module12.src.Car import Car
from Module12.src.Bicycle import Bicycle
from Module12.src.Motorcycle import Motorcycle


if __name__ == '__main__':
    bicycle = Bicycle()
    motorcycle = Motorcycle()
    car = Car()

    print(bicycle.ride())
    print(bicycle.rider())

    print(motorcycle.ride())
    print(motorcycle.rider())

    print(car.ride())
    print(car.rider())
