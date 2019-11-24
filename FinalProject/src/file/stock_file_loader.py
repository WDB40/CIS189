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
        self.all_five_year_revs = {}
        self.all_five_year_earnings = {}
        self.all_five_year_divs = {}
        self.all_div_yields = {}
        self.all_price_books = {}
        self.all_price_sales = {}
        self.all_market_caps = {}
        self.all_volumes = {}
        self.all_incomes = {}
        self.all_ROAs = {}
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
                five_year_rev = RankingRecord(row[0], row[9], row[10])
                five_year_earnings = RankingRecord(row[0], row[11], row[12])
                five_year_div = RankingRecord(row[0], row[13], row[14])
                div_yield = RankingRecord(row[0], row[15], row[16])
                price_book = RankingRecord(row[0], row[17], row[18])
                price_sales = RankingRecord(row[0], row[19], row[20])
                market_cap = RankingRecord(row[0], row[21], row[22])
                volume = RankingRecord(row[0], row[23], row[24])
                income = RankingRecord(row[0], row[25], row[26])
                roa = RankingRecord(row[0], row[27], row[28])

                self.all_stocks[stock.ticker] = stock
                self.all_recent_earnings[recent_earnings.ticker] = recent_earnings
                self.all_past_year_earnings[past_year_earnings.ticker] = past_year_earnings
                self.all_pe_ratios[pe_ratio.ticker] = pe_ratio
                self.all_five_year_revs[five_year_rev.ticker] = five_year_rev
                self.all_five_year_earnings[five_year_earnings.ticker] = five_year_earnings
                self.all_five_year_divs[five_year_div.ticker] = five_year_div
                self.all_div_yields[div_yield.ticker] = div_yield
                self.all_price_books[price_book.ticker] = price_book
                self.all_price_sales[price_sales.ticker] = price_sales
                self.all_market_caps[market_cap.ticker] = market_cap
                self.all_volumes[volume.ticker] = volume
                self.all_incomes[income.ticker] = income
                self.all_ROAs[roa.ticker] = roa

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

        for value in self.all_five_year_revs.values():
            self.database.insert_five_year_rev(value.ticker, value.factor, value.rank)

        for value in self.all_five_year_earnings.values():
            self.database.insert_five_year_earnings(value.ticker, value.factor, value.rank)

        for value in self.all_five_year_divs.values():
            self.database.insert_five_year_div(value.ticker, value.factor, value.rank)

        for value in self.all_div_yields.values():
            self.database.insert_div_yield(value.ticker, value.factor, value.rank)

        for value in self.all_price_books.values():
            self.database.insert_price_book(value.ticker, value.factor, value.rank)

        for value in self.all_price_sales.values():
            self.database.insert_price_sales(value.ticker, value.factor, value.rank)

        for value in self.all_market_caps.values():
            self.database.insert_market_cap(value.ticker, value.factor, value.rank)

        for value in self.all_volumes.values():
            self.database.insert_volume(value.ticker, value.factor, value.rank)

        for value in self.all_incomes.values():
            self.database.insert_income(value.ticker, value.factor, value.rank)

        for value in self.all_ROAs.values():
            self.database.insert_roa(value.ticker, value.factor, value.rank)
