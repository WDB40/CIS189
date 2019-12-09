"""
Program: stock_database.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Used for interacting with the database
"""


import sqlite3
from sqlite3 import Error
from FinalProject.src.database.stock_queries import *


class StockDatabase:

    DATABASE_NAME = "stockDatabase.db"

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
        self.create_table(pe_ratio_table_query)
        self.create_table(five_year_rev_table_query)
        self.create_table(five_year_earnings_table_query)
        self.create_table(five_year_div_table_query)
        self.create_table(div_yield_table_query)
        self.create_table(price_book_table_query)
        self.create_table(price_sales_table_query)
        self.create_table(market_cap_table_query)
        self.create_table(volume_table_query)
        self.create_table(income_table_query)
        self.create_table(roa_table_query)
        self.create_table(debt_equity_table_query)
        self.create_table(profit_table_query)

    def insert_record(self, sql_statement, insert):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(sql_statement, insert)

    def return_records(self, sql_statement):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(sql_statement)
            return cursor.fetchall()

    def insert_stock_base(self, ticker, name, last_price):
        insert = (ticker, name, last_price)
        self.insert_record(insert_stock_base_query, insert)

    def get_all_stock_base(self):
        return self.return_records(view_all_base_stock_query)

    def insert_recent_earnings(self, ticker, earnings, rank):
        insert = (ticker, earnings, rank)
        self.insert_record(insert_recent_earnings_query, insert)

    def get_all_recent_earnings(self):
        return self.return_records(view_all_recent_earnings_query)

    def insert_past_year_earnings(self, ticker, earnings, rank):
        insert = (ticker, earnings, rank)
        self.insert_record(insert_past_year_earnings_query, insert)

    def get_all_past_year_earnings(self):
        return self.return_records(view_all_past_year_earnings_query)

    def insert_pe_ratio(self, ticker, ratio, rank):
        insert = (ticker, ratio, rank)
        self.insert_record(insert_pe_ratio_query, insert)

    def get_all_pe_ratio(self):
        return self.return_records(view_all_pe_ratio_query)

    def insert_five_year_rev(self, ticker, rev, rank):
        insert = (ticker, rev, rank)
        self.insert_record(insert_five_year_rev_query, insert)

    def get_all_five_year_rev(self):
        return self.return_records(view_all_five_year_rev_query)

    def insert_five_year_earnings(self, ticker, earnings, rank):
        insert = (ticker, earnings, rank)
        self.insert_record(insert_five_year_earnings_query, insert)

    def get_all_five_year_earnings(self):
        return self.return_records(view_all_five_year_earnings_query)

    def insert_five_year_div(self, ticker, div, rank):
        insert = (ticker, div, rank)
        self.insert_record(insert_five_year_div_query, insert)

    def get_all_five_year_div(self):
        return self.return_records(view_all_five_year_div_query)

    def insert_div_yield(self, ticker, div, rank):
        insert = (ticker, div, rank)
        self.insert_record(insert_div_yield_query, insert)

    def get_all_div_yield(self):
        return self.return_records(view_all_div_yield_query)

    def insert_price_book(self, ticker, ratio, rank):
        insert = (ticker, ratio, rank)
        self.insert_record(insert_price_book_query, insert)

    def get_all_price_book(self):
        return self.return_records(view_all_price_book_query)

    def insert_price_sales(self, ticker, ratio, rank):
        insert = (ticker, ratio, rank)
        self.insert_record(insert_price_sales_query, insert)

    def get_all_price_sales(self):
        return self.return_records(view_all_price_sales_query)

    def insert_market_cap(self, ticker, market_cap, rank):
        insert = (ticker, market_cap, rank)
        self.insert_record(insert_market_cap_query, insert)

    def get_all_market_cap(self):
        return self.return_records(view_all_market_cap_query)

    def insert_volume(self, ticker, volume, rank):
        insert = (ticker, volume, rank)
        self.insert_record(insert_volume_query, insert)

    def get_all_volume(self):
        return self.return_records(view_all_volume_query)

    def insert_income(self, ticker, income, rank):
        insert = (ticker, income, rank)
        self.insert_record(insert_income_query, insert)

    def get_all_income(self):
        return self.return_records(view_all_income_query)

    def insert_roa(self, ticker, roa, rank):
        insert = (ticker, roa, rank)
        self.insert_record(insert_roa_query, insert)

    def get_all_roa(self):
        return self.return_records(view_all_roa_query)

    def insert_debt_equity(self, ticker, ratio, rank):
        insert = (ticker, ratio, rank)
        self.insert_record(insert_debt_equity_query, insert)

    def get_all_debt_equity(self):
        return self.return_records(view_all_debt_equity_query)

    def insert_profit(self, ticker, profit, rank):
        insert = (ticker, profit, rank)
        self.insert_record(insert_profit_query, insert)

    def get_all_profit(self):
        return self.return_records(view_all_profit_query)
