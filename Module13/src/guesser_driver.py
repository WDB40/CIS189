"""
Program: guesser_driver.py
Author: Wes Brown
Last date modified: 11/19/19

Purpose: Driving the number guesser game
"""

import tkinter
from tkinter import messagebox
from random import randint


def select_number(value):
    buttons[value].config(state="disabled")
    if value == winning_number:
        messagebox.showinfo("Winner!", f"You selected the correct number: {value}")
        reset_game()


def reset_game():
    for button in buttons.values():
        button.config(state="normal")
    global winning_number
    winning_number = randint(0, 10)


if __name__ == '__main__':
    winning_number = randint(0, 10)

    buttons = {}

    game = tkinter.Tk()
    game.title("Number Guesser Game")

    label = tkinter.Label(game, text="Guess a number!")
    label.grid(row=0)

    for i in range(1, 11):
        buttons[i] = tkinter.Button(game, text=f"{i}")
        buttons[i].config(command=lambda value=i: select_number(value))
        buttons[i].grid(row=i)

    game.mainloop()
