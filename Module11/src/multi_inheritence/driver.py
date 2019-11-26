"""
Program: gui_driver.py
Author: Wes Brown
Last date modified: 11/04/19

Purpose: Driver the class for manager
"""
from datetime import datetime

from Module11.src.multi_inheritence.manager import Manager


if __name__ == '__main__':
    manager_me = Manager("Brown", "Wes", "111 Main Street", "555-555-5555", datetime.today(), 40000, "Technology", ["Peter Jones", "Samantha Thompson", "Madison Peters"])
    # This will use the display on the manager
    print(manager_me.display())
    manager_me.give_raise(2000)
    # This will again use the display on the manager
    print(manager_me.display())

    del manager_me
