import sqlite3
from sqlite3 import Error
from FinalProject.src.database.stock_queries import *


class StockDatabase:

    DATABASE_NAME = "testStockDatabase.db"

    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.DATABASE_NAME)
            return conn
        except Error as error:
            print(error)
            return None

    def create_table(self, sql_statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_statement)
        except Error as error:
            print(error)

    def initialize_database(self):
        self.create_table(stock_base_table_query)
        self.create_table(recent_earnings_table_query)
        self.create_table(past_year_earnings_table_query)

    def insert_stock_base(self, ticker, name, last_price):
        insert = (ticker, name, last_price)
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(insert_stock_base_query, insert)

    def get_all_stock_base(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(view_all_base_stock_query)
            return cursor.fetchall()

    def insert_recent_earnings(self, ticker, earnings, rank):
        insert = (ticker, earnings, rank)
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(insert_recent_earnings_query, insert)

    def get_all_recent_earnings(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(view_all_recent_earnings_query)
            return cursor.fetchall()

    def insert_past_year_earnings(self, ticker, earnings, rank):
        insert = (ticker, earnings, rank)
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(insert_past_year_earnings_query, insert)

    def get_all_past_year_earnings(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(view_all_past_year_earnings_query)
            return cursor.fetchall()
