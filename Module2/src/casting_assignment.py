"""
Program: casting_assignment.py
Author: Wes Brown
Last date modified: 09/02/19

The purpose of this program is to accept any input, convert to a integer type and output the integer.
"""

test1 = "5"
test2 = 10.5
test3 = "10.5"
test4 = "Not a number"
test5 = "10five"

"""
       Expected    Actual
test1: 5           5
test2: 10          10
test3: 10          error
test4: error       error
test5: error       error
"""

print(int(test1))
print(int(test2))
# print(int(test3))
# print(int(test4))
# print(int(test5))
