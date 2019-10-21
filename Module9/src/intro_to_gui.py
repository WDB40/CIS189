"""
Program: intro_to_gui.py
Author: Wes Brown
Last date modified: 10/20/19

Purpose: Introducing the basics of GUIs in python
"""


import tkinter


def pick_cis():
    label.config(text="Nice choice")


def pick_bis():
    label.config(text="Are you sure?")


if __name__ == '__main__':
    m = tkinter.Tk()

    # m.title("Counting Sheep")
    # button = tkinter.Button(m, text="Stop", width=25, command=m.destroy)
    # button.pack()

    m.title("Major Decision")
    label = tkinter.Label(m, text="No Selection Made")
    label.grid(row=4)
    var1 = tkinter.IntVar()
    check = tkinter.Checkbutton(m, text="CIS", variable=var1, command=pick_cis).grid(row=0)
    var2 = tkinter.IntVar()
    check = tkinter.Checkbutton(m, text="BIS", variable=var2, command=pick_bis).grid(row=1)
    exit_button = tkinter.Button(m, text="Exit", width=25, command=m.destroy)
    exit_button.grid(row=5)

    m.mainloop()
