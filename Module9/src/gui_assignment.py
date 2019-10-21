"""
Program: gui_assignment.py
Author: Wes Brown
Last date modified: 10/20/19

Purpose: Introducing the basics of GUIs in python
"""


import tkinter


def finally_picked():
    waiting_lab.config(text="About time you picked...")


if __name__ == '__main__':
    pop_up = tkinter.Tk()

    pop_up.title("Favorite Meal")

    breakfast_cb = tkinter.Checkbutton(pop_up, text="Breakfast", command=finally_picked).grid(row=1)
    second_breakfast_cb = tkinter.Checkbutton(pop_up, text="Second Breakfast", command=finally_picked).grid(row=2)
    lunch_cb = tkinter.Checkbutton(pop_up, text="Lunch", command=finally_picked).grid(row=3)
    dinner_cb = tkinter.Checkbutton(pop_up, text="Dinner", command=finally_picked).grid(row=4)

    waiting_lab = tkinter.Label(pop_up, text="Waiting", width=35)
    waiting_lab.grid(row=5)

    exit_button = tkinter.Button(pop_up, text="Exit", width=25, command=pop_up.destroy)
    exit_button.grid(row=6)

    pop_up.mainloop()
