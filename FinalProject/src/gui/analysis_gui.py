import tkinter
from FinalProject.src.analysis.selector import Selector


class AnalysisGUI(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Simple Stock Analysis")
        tkinter.Label(self, text="Please select FIVE factors to create an analysis from:").pack()

        self.recent_earnings = tkinter.BooleanVar()
        self.past_year_earnings = tkinter.BooleanVar()
        self.pe_ratio = tkinter.BooleanVar()
        self.five_year_rev = tkinter.BooleanVar()
        self.five_year_earnings = tkinter.BooleanVar()
        self.five_year_div = tkinter.BooleanVar()
        self.div_yield = tkinter.BooleanVar()
        self.price_book = tkinter.BooleanVar()
        self.price_sales = tkinter.BooleanVar()
        self.market_cap = tkinter.BooleanVar()
        self.volume = tkinter.BooleanVar()
        self.income = tkinter.BooleanVar()
        self.roa = tkinter.BooleanVar()
        self.debt_equity = tkinter.BooleanVar()
        self.profit = tkinter.BooleanVar()

        self.check_frame = tkinter.Frame(self)
        self.check_frame.pack(side=tkinter.TOP)

        self.earnings_frame = tkinter\
            .LabelFrame(self.check_frame, text="Earnings", padx=5, pady=5)
        self.earnings_frame.pack(padx=10, pady=10, side=tkinter.LEFT)

        self.recent_earnings_check = tkinter\
            .Checkbutton(self.earnings_frame, text="Most Recent", offvalue=False, onvalue=True, variable=self.recent_earnings, command=self.on_select)
        self.recent_earnings_check.pack()

        self.past_year_earnings_check = tkinter\
            .Checkbutton(self.earnings_frame, text="Past Year", offvalue=False, onvalue=True, variable=self.past_year_earnings, command=self.on_select)
        self.past_year_earnings_check.pack()

        self.pe_ratio_check = tkinter\
            .Checkbutton(self.earnings_frame, text="Price to Earnings Ratio", offvalue=False, onvalue=True, variable=self.pe_ratio, command=self.on_select)
        self.pe_ratio_check.pack()

        self.growth_frame = tkinter\
            .LabelFrame(self.check_frame, text="Growth", padx=5, pady=5)
        self.growth_frame.pack(padx=10, pady=10, side=tkinter.LEFT)

        self.growth_label = tkinter\
            .Label(self.growth_frame, text="Over past 5 years:")
        self.growth_label.pack()

        self.five_year_rev_check = tkinter\
            .Checkbutton(self.growth_frame, text="Revenue", offvalue=False, onvalue=True, variable=self.five_year_rev, command=self.on_select)
        self.five_year_rev_check.pack()

        self.five_year_earnings_check = tkinter\
            .Checkbutton(self.growth_frame, text="Earnings", offvalue=False, onvalue=True, variable=self.five_year_earnings, command=self.on_select)
        self.five_year_earnings_check.pack()

        self.five_year_div_check = tkinter\
            .Checkbutton(self.growth_frame, text="Dividend", offvalue=False, onvalue=True, variable=self.five_year_div, command=self.on_select)
        self.five_year_div_check.pack()

        self.stability_frame = tkinter\
            .LabelFrame(self.check_frame, text="Stability", padx=5, pady=5)
        self.stability_frame.pack(padx=10, pady=10, side=tkinter.LEFT)

        self.div_yield_check = tkinter\
            .Checkbutton(self.stability_frame, text="Dividend Yield", offvalue=False, onvalue=True, variable=self.div_yield, command=self.on_select)
        self.div_yield_check.pack()

        self.price_book_check = tkinter\
            .Checkbutton(self.stability_frame, text="Price to Book Ratio", offvalue=False, onvalue=True, variable=self.price_book, command=self.on_select)
        self.price_book_check.pack()

        self.price_sales_check = tkinter\
            .Checkbutton(self.stability_frame, text="Price to Sales Ratio", offvalue=False, onvalue=True, variable=self.price_sales, command=self.on_select)
        self.price_sales_check.pack()

        self.size_frame = tkinter\
            .LabelFrame(self.check_frame, text="Size", padx=5, pady=5)
        self.size_frame.pack(padx=10, pady=10, side=tkinter.LEFT)

        self.market_cap_check = tkinter\
            .Checkbutton(self.size_frame, text="Market Capitalization", offvalue=False, onvalue=True, variable=self.market_cap, command=self.on_select)
        self.market_cap_check.pack()

        self.volume_check = tkinter\
            .Checkbutton(self.size_frame, text="Trade Volume", offvalue=False, onvalue=True, variable=self.volume, command=self.on_select)
        self.volume_check.pack()

        self.income_check = tkinter\
            .Checkbutton(self.size_frame, text="Net Income", offvalue=False, onvalue=True, variable=self.income, command=self.on_select)
        self.income_check.pack()

        self.financials_frame = tkinter\
            .LabelFrame(self.check_frame, text="Financials", padx=5, pady=5)
        self.financials_frame.pack(padx=10, pady=10, side=tkinter.LEFT)

        self.roa_check = tkinter\
            .Checkbutton(self.financials_frame, text="Return on Assets", offvalue=False, onvalue=True, variable=self.roa, command=self.on_select)
        self.roa_check.pack()

        self.debt_equity_check = tkinter\
            .Checkbutton(self.financials_frame, text="Debt to Equity Ratio", offvalue=False, onvalue=True, variable=self.debt_equity, command=self.on_select)
        self.debt_equity_check.pack()

        self.profit_check = tkinter\
            .Checkbutton(self.financials_frame, text="Profit Margin", offvalue=False, onvalue=True, variable=self.profit, command=self.on_select)
        self.profit_check.pack()

        self.button_frame = tkinter.Frame(self, padx=10, pady=10)
        self.button_frame.pack(side=tkinter.BOTTOM)

        self.create_analysis_button = tkinter\
            .Button(self.button_frame, text="Create Analysis", state=tkinter.DISABLED)
        self.create_analysis_button.pack(side=tkinter.LEFT, padx=5, pady=5)

        self.close_button = tkinter\
            .Button(self.button_frame, text="Close", command=self.destroy)
        self.close_button.pack(side=tkinter.LEFT, padx=5, pady=5)

    def enable_all_checks(self):
        self.recent_earnings_check.config(state=tkinter.NORMAL)
        self.past_year_earnings_check.config(state=tkinter.NORMAL)
        self.pe_ratio_check.config(state=tkinter.NORMAL)
        self.five_year_rev_check.config(state=tkinter.NORMAL)
        self.five_year_earnings_check.config(state=tkinter.NORMAL)
        self.five_year_div_check.config(state=tkinter.NORMAL)
        self.div_yield_check.config(state=tkinter.NORMAL)
        self.price_book_check.config(state=tkinter.NORMAL)
        self.price_sales_check.config(state=tkinter.NORMAL)
        self.market_cap_check.config(state=tkinter.NORMAL)
        self.volume_check.config(state=tkinter.NORMAL)
        self.income_check.config(state=tkinter.NORMAL)
        self.roa_check.config(state=tkinter.NORMAL)
        self.debt_equity_check.config(state=tkinter.NORMAL)
        self.profit_check.config(state=tkinter.NORMAL)

    def disable_non_selected(self):
        if not self.recent_earnings.get():
            self.recent_earnings_check.config(state=tkinter.DISABLED)
        if not self.past_year_earnings.get():
            self.past_year_earnings_check.config(state=tkinter.DISABLED)
        if not self.pe_ratio.get():
            self.pe_ratio_check.config(state=tkinter.DISABLED)
        if not self.five_year_rev.get():
            self.five_year_rev_check.config(state=tkinter.DISABLED)
        if not self.five_year_earnings.get():
            self.five_year_earnings_check.config(state=tkinter.DISABLED)
        if not self.five_year_div.get():
            self.five_year_div_check.config(state=tkinter.DISABLED)
        if not self.div_yield.get():
            self.div_yield_check.config(state=tkinter.DISABLED)
        if not self.price_book.get():
            self.price_book_check.config(state=tkinter.DISABLED)
        if not self.price_sales.get():
            self.price_sales_check.config(state=tkinter.DISABLED)
        if not self.market_cap.get():
            self.market_cap_check.config(state=tkinter.DISABLED)
        if not self.volume.get():
            self.volume_check.config(state=tkinter.DISABLED)
        if not self.income.get():
            self.income_check.config(state=tkinter.DISABLED)
        if not self.roa.get():
            self.roa_check.config(state=tkinter.DISABLED)
        if not self.debt_equity.get():
            self.debt_equity_check.config(state=tkinter.DISABLED)
        if not self.profit.get():
            self.profit_check.config(state=tkinter.DISABLED)

    def on_select(self):
        count = 0

        if self.recent_earnings.get():
            count = count + 1
        if self.past_year_earnings.get():
            count = count + 1
        if self.pe_ratio.get():
            count = count + 1
        if self.five_year_rev.get():
            count = count + 1
        if self.five_year_earnings.get():
            count = count + 1
        if self.five_year_div.get():
            count = count + 1
        if self.div_yield.get():
            count = count + 1
        if self.price_book.get():
            count = count + 1
        if self.price_sales.get():
            count = count + 1
        if self.market_cap.get():
            count = count + 1
        if self.volume.get():
            count = count + 1
        if self.income.get():
            count = count + 1
        if self.roa.get():
            count = count + 1
        if self.debt_equity.get():
            count = count + 1
        if self.profit.get():
            count = count + 1

        if count == 5:
            self.disable_non_selected()
            self.create_analysis_button.config(state=tkinter.NORMAL)
        else:
            self.enable_all_checks()
            self.create_analysis_button.config(state=tkinter.DISABLED)
