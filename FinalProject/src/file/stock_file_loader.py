import csv
from FinalProject.src.model.stock_record import StockRecord
from FinalProject.src.model.ranking_record import RankingRecord
from FinalProject.src.database.stock_database import StockDatabase


class StockFileLoader:
    FILENAME = "C:\\Users\\wbrow\\PycharmProjects\\CIS189\\FinalProject\\src\\file\\ProjectData.csv"

    def __init__(self):
        self.all_stocks = {}
        self.all_recent_earnings = {}
        self.database = StockDatabase()

    def read_file(self):
        with open(self.FILENAME) as stock_file:
            csv_reader = csv.reader(stock_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count = 1
                    continue

                stock = StockRecord(row[0], row[1], row[2])
                recent_earnings = RankingRecord(row[0], row[3], row[4])

                self.all_stocks[stock.ticker] = stock
                self.all_recent_earnings[recent_earnings.ticker] = recent_earnings

    def load_to_database(self):
        self.read_file()
        for value in self.all_stocks.values():
            self.database.insert_stock_base(value.ticker, value.name, value.last_price)
        for value in self.all_recent_earnings.values():
            self.database.insert_recent_earnings(value.ticker, value.factor, value.rank)
