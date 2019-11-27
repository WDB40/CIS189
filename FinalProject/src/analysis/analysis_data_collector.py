from FinalProject.src.database.stock_database import StockDatabase


class AnalysisDataCollector:
    def __init__(self, selector):
        self.selector = selector
        self.database = StockDatabase()
        self.stock_data = {}

    def add_recent_earnings(self):
        self.stock_data["Recent Earnings"] = self.database.get_all_recent_earnings()

    def add_past_year_earnings(self):
        self.stock_data["Past Year Earnings"] = self.database.get_all_past_year_earnings()

    def add_pe_ratio(self):
        self.stock_data["P/E Ratio"] = self.database.get_all_pe_ratio()

    def add_five_year_rev(self):
        self.stock_data["5 Year Rev Change"] = self.database.get_all_five_year_rev()

    def add_five_year_earnings(self):
        self.stock_data["5 Year Earnings Change"] = self.database.get_all_five_year_earnings()

    def add_five_year_div(self):
        self.stock_data["5 Year Dividend Change"] = self.database.get_all_five_year_div()

    def add_div_yield(self):
        self.stock_data["Dividend Yield"] = self.database.get_all_div_yield()

    def add_price_book(self):
        self.stock_data["Price/Book Ratio"] = self.database.get_all_price_book()

    def add_price_sales(self):
        self.stock_data["Price/Sales Ratio"] = self.database.get_all_price_sales()

    def add_market_cap(self):
        self.stock_data["Market Cap"] = self.database.get_all_market_cap()

    def add_volume(self):
        self.stock_data["Volume"] = self.database.get_all_volume()

    def add_income(self):
        self.stock_data["Net Income"] = self.database.get_all_income()

    def add_roa(self):
        self.stock_data["Return on Assets"] = self.database.get_all_roa()

    def add_debt_equity(self):
        self.stock_data["Debt/Equity Ratio"] = self.database.get_all_debt_equity()

    def add_profit(self):
        self.stock_data["Profit Margin"] = self.database.get_all_profit()

    def get_analysis_data(self):
        if self.selector.validate_state() is False:
            raise AttributeError("Incorrect number of factors selected.")

        if self.selector.recent_earnings:
            self.add_recent_earnings()
        if self.selector.past_year_earnings:
            self.add_past_year_earnings()
        if self.selector.pe_ratio:
            self.add_pe_ratio()
        if self.selector.five_year_rev:
            self.add_five_year_rev()
        if self.selector.five_year_earnings:
            self.add_five_year_earnings()
        if self.selector.five_year_div:
            self.add_five_year_div()
        if self.selector.div_yield:
            self.add_div_yield()
        if self.selector.price_book:
            self.add_price_book()
        if self.selector.price_sales:
            self.add_price_sales()
        if self.selector.market_cap:
            self.add_market_cap()
        if self.selector.volume:
            self.add_volume()
        if self.selector.income:
            self.add_income()
        if self.selector.roa:
            self.add_roa()
        if self.selector.debt_equity:
            self.add_debt_equity()
        if self.selector.profit:
            self.add_profit()

        return self.stock_data
