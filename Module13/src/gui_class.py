"""
Program: gui_class.py
Author: Wes Brown
Last date modified: 11/23/19

Purpose: Class for making the gui interaction easier
"""


import tkinter
from Module13.src.using_database import *
import datetime


class GUI(tkinter.Tk):

    DATABASE = "guidatabase.db"

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Interacting with Database")

        self.button_create_database = tkinter\
            .Button(self, text="Create Database & Tables", command=self.initialize_database)\
            .grid(row=1, column=0, columnspan=2)

        self.first_name_label = tkinter\
            .Label(self, text="First Name: ")\
            .grid(row=2, column=0)

        self.first_name_text = tkinter\
            .Entry(self)
        self.first_name_text.grid(row=2, column=1)

        self.last_name_label = tkinter\
            .Label(self, text="Last Name: ")\
            .grid(row=3, column=0)

        self.last_name_text = tkinter\
            .Entry(self)
        self.last_name_text.grid(row=3, column=1)

        self.major_label = tkinter\
            .Label(self, text="Major: ")\
            .grid(row=4, column=0)

        self.major_text = tkinter\
            .Entry(self)
        self.major_text.grid(row=4, column=1)

        self.start_date_label = tkinter\
            .Label(self, text="Start Date: ")\
            .grid(row=5, column=0)

        self.start_date_text = tkinter\
            .Entry(self)
        self.start_date_text.grid(row=5, column=1)

        self.insert_person_button = tkinter\
            .Button(self, text="Insert Person", command=self.insert_person_gui)\
            .grid(row=6, column=0)

        self.insert_student_button = tkinter\
            .Button(self, text="Insert Student", command=self.insert_student_gui)\
            .grid(row=6, column=1)

        self.view_persons_button = tkinter\
            .Button(self, text="View All Persons", command=self.print_persons)\
            .grid(row=7, column=0)

        self.view_students_button = tkinter\
            .Button(self, text="View All Students", command=self.print_students)\
            .grid(row=7, column=1)

        self.close_button = tkinter\
            .Button(self, text="Close", command=self.destroy)\
            .grid(row=8, column=0, columnspan=2)

    def initialize_database(self):
        create_tables(self.DATABASE)

    def insert_person_gui(self):
        self.validate_person()
        connection = create_connection(self.DATABASE)
        with connection:
            person = (self.first_name_text.get(), self.last_name_text.get())
            insert_person(connection, person)

    def print_persons(self):
        connection = create_connection(self.DATABASE)
        persons = select_all_persons(connection)
        for person in persons:
            print(person)

    def insert_student_gui(self):
        self.validate_student()
        connection = create_connection(self.DATABASE)
        with connection:
            person_id = get_person_id(connection, self.first_name_text.get(), self.last_name_text.get())
            if person_id is None:
                person = (self.first_name_text.get(), self.last_name_text.get())
                person_id = insert_person(connection, person)
            student = (person_id, self.major_text.get(), self.start_date_text.get())
            insert_student(connection, student)

    def print_students(self):
        connection = create_connection(self.DATABASE)
        students = select_all_students(connection)
        for student in students:
            print(student)

    def validate_person(self):
        firstname = self.first_name_text.get()
        lastname = self.last_name_text.get()
        if firstname == "" or lastname == "":
            raise ValueError("First name and last name are required for both person and student.")

    def validate_student(self):
        self.validate_person()
        major = self.major_text.get()
        start_date = self.start_date_text.get()
        if major == "" or start_date == "":
            raise ValueError("Major and start date are required for student.")
        try:
            converted_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Start date must be formatted properly")
