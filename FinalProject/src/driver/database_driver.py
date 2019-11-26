from FinalProject.src.database.stock_database import StockDatabase
from FinalProject.src.file.stock_file_loader import StockFileLoader

if __name__ == '__main__':
    database = StockDatabase()
    database.initialize_database()
    file_loader = StockFileLoader()
    file_loader.load_to_database()
