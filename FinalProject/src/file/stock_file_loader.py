import csv
from FinalProject.src.model.stock_record import StockRecord
from FinalProject.src.model.ranking_record import RankingRecord
from FinalProject.src.database.stock_database import StockDatabase


class StockFileLoader:
    FILENAME = "C:\\Users\\wbrow\\PycharmProjects\\CIS189\\FinalProject\\src\\file\\ProjectData.csv"

    def __init__(self):
        self.all_stocks = {}
        self.all_recent_earnings = {}
        self.all_past_year_earnings = {}
        self.all_pe_ratios = {}
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
                past_year_earnings = RankingRecord(row[0], row[5], row[6])
                pe_ratio = RankingRecord(row[0], row[7], row[8])

                self.all_stocks[stock.ticker] = stock
                self.all_recent_earnings[recent_earnings.ticker] = recent_earnings
                self.all_past_year_earnings[past_year_earnings.ticker] = past_year_earnings
                self.all_pe_ratios[pe_ratio.ticker] = pe_ratio

    def load_to_database(self):
        self.read_file()
        for value in self.all_stocks.values():
            self.database.insert_stock_base(value.ticker, value.name, value.last_price)
        for value in self.all_recent_earnings.values():
            self.database.insert_recent_earnings(value.ticker, value.factor, value.rank)
        for value in self.all_past_year_earnings.values():
            self.database.insert_past_year_earnings(value.ticker, value.factor, value.rank)
        for value in self.all_pe_ratios.values():
            self.database.insert_pe_ratio(value.ticker, value.factor, value.rank)
