"""
Program: guesser_driver.py
Author: Wes Brown
Last date modified: 11/19/19

Purpose: Driving the number guesser game
"""

import tkinter
from tkinter import messagebox
from random import randint
from Module13.src.number_guesser import NumberGuesser
import math

NUMBER_OPTIONS = 20
NUMBER_COLUMNS = 5


def select_number(value):
    buttons[value].config(state="disabled")
    if value == winning_number:
        messagebox.showinfo("Winner!", f"You selected the correct number: {value}")
        reset_game()
    else:
        global guesses
        guesses.add_guess(value)


def reset_game():
    for button in buttons.values():
        button.config(state="normal")
    create_new_winning_number()
    global guesses
    guesses = NumberGuesser()


def create_new_winning_number():
    global winning_number
    winning_number = randint(0, NUMBER_OPTIONS)


def get_row(value):
    return math.ceil(value / NUMBER_COLUMNS)


def get_column(value):
    if value % NUMBER_COLUMNS == 0:
        return NUMBER_COLUMNS - 1
    else:
        return (value - (math.floor(value / NUMBER_COLUMNS) * NUMBER_COLUMNS)) - 1


if __name__ == '__main__':
    winning_number = 0
    create_new_winning_number()
    guesses = NumberGuesser()

    buttons = {}

    game = tkinter.Tk()
    game.title("Number Guesser Game")

    label = tkinter.Label(game, text="Guess a number!")
    label.grid(row=0, columnspan=NUMBER_COLUMNS-1)

    for i in range(1, NUMBER_OPTIONS + 1):
        buttons[i] = tkinter.Button(game, text=f"{i}")
        buttons[i].config(command=lambda value=i: select_number(value))
        buttons[i].grid(row=get_row(i), column=get_column(i))

    close_button = tkinter.Button(game, text="Close Game", command=game.destroy).grid(row=NUMBER_OPTIONS, columnspan=NUMBER_COLUMNS-1)

    game.mainloop()
