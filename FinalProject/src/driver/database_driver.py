"""
Program: database_driver.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Used for creating the database and loading the data from the file
"""


from FinalProject.src.database.stock_database import StockDatabase
from FinalProject.src.file.stock_file_loader import StockFileLoader

if __name__ == '__main__':
    database = StockDatabase()
    database.initialize_database()
    file_loader = StockFileLoader()
    file_loader.load_to_database()
