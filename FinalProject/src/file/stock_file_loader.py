import csv
from FinalProject.src.model.stock_record import StockRecord
from FinalProject.src.database.stock_database import StockDatabase


class StockFileLoader:
    FILENAME = "C:\\Users\\wbrow\\PycharmProjects\\CIS189\\FinalProject\\src\\file\\ProjectData.csv"

    def __init__(self):
        self.records = {}
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
                self.records[stock.ticker] = stock

        return self.records

    def load_to_database(self):
        self.read_file()
        for record in self.records.values():
            self.database.insert_stock_base(record.ticker, record.name, record.last_price)
