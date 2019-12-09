"""
Program: filename_validator.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Used for validating the name of a file that is entered via the GUI
"""


class FilenameValidator:
    def __init__(self):
        self.valid = False
        self.error_text = ""

    def validate(self, filename):
        if filename == "":
            self.valid = False
            self.error_text = "Please enter a filename."
        elif not filename.isalpha():
            self.valid = False
            self.error_text = "Alpha characters only for filename."
        else:
            self.valid = True

        return self.valid

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    @property
    def error_text(self):
        return self._error_text

    @error_text.setter
    def error_text(self, value):
        self._error_text = value
