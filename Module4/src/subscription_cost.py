"""
Program: subscription_cost.py
Author: Wes Brown
Last date modified: 09/10/19

Purpose: To receive a subscription level and print the cost.
"""


def print_subscription_cost():
    level = input("Enter the subscription level: ").capitalize()
    cost = -1

    if level == "Platinum":
        cost = 60
    elif level == "Gold":
        cost = 50
    elif level == "Silver":
        cost = 40
    elif level == "Bronze":
        cost = 30
    elif level == "Free":
        cost = 0

    return cost


if __name__ == '__main__':
    print_subscription_cost()
