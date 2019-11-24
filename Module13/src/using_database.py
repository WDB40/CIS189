"""
Program: using_database.py
Author: Wes Brown
Last date modified: 11/23/19

Purpose: Using a sqlite database in python
"""


import sqlite3
from sqlite3 import Error


def create_connection(database_name):
    try:
        connection = sqlite3.connect(database_name)
        return connection
    except Error as error:
        print(error)
        return None


def create_table(connection, sql_statement):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_statement)
    except Error as error:
        print(error)


def create_tables(database):
    sql_create_person_table = """CREATE TABLE IF NOT EXISTS person (
                                    id INTEGER PRIMARY KEY,
                                    firstname TEXT NOT NULL,
                                    lastname TEXT NOT NULL);"""

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id INTEGER PRIMARY KEY,
                                    major TEXT NOT NULL,
                                    begin_date TEXT NOT NULL,
                                    end_date TEXT,
                                    FOREIGN KEY (id) REFERENCES person (id));"""

    connection = create_connection(database)
    if connection is not None:
        create_table(connection, sql_create_person_table)
        create_table(connection, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def insert_person(connection, person):
    sql_statement = """INSERT INTO person(firstname, lastname)
                            VALUES(?, ?);"""
    cursor = connection.cursor()
    cursor.execute(sql_statement, person)
    return cursor.lastrowid


def insert_student(connection, student):
    sql_statement = """INSERT INTO student(id, major, begin_date)
                            VALUES(?, ?, ?);"""
    cursor = connection.cursor()
    cursor.execute(sql_statement, student)
    return cursor.lastrowid


def select_all_persons(connection):
    sql_statement = "SELECT * FROM person;"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    return cursor.fetchall()


def select_all_students(connection):
    sql_statement = "SELECT * FROM student;"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    return cursor.fetchall()


def get_person_id(connection, firstname, lastname):
    sql_statement = """SELECT id FROM person
                            WHERE firstname = ? AND lastname = ?;"""
    person = (firstname, lastname)
    cursor = connection.cursor()
    cursor.execute(sql_statement, person)
    id = cursor.fetchone()
    if id is not None:
        return id[0]
    else:
        return id
