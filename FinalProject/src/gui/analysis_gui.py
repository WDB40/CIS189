import tkinter
from tkinter import messagebox
from FinalProject.src.validators.selector import Selector
from FinalProject.src.validators.filename_validator import FilenameValidator
from FinalProject.src.analysis.analysis_data_collector import AnalysisDataCollector
from FinalProject.src.analysis.analysis_data_aggregator import AnalysisDataAggregator
from FinalProject.src.file.analysis_file_printer import AnalysisFilePrinter


class AnalysisGUI(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Simple Stock Analysis")
        tkinter.Label(self, text="Please select FIVE factors to create an analysis from:").pack()

        self.selector = Selector()

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

        self.input_frame = tkinter.Frame(self)
        self.input_frame.pack(side=tkinter.TOP)

        self.check_frame = tkinter.Frame(self.input_frame)
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

        self.filename_frame = tkinter\
            .Frame(self.input_frame)
        self.filename_frame.pack(side=tkinter.BOTTOM)

        self.filename_label = tkinter\
            .Label(self.filename_frame, text="Enter Analysis Name:")
        self.filename_label.pack(side=tkinter.LEFT)

        self.filename_entry = tkinter\
            .Entry(self.filename_frame)
        self.filename_entry.pack(side=tkinter.LEFT)

        self.filename_error = tkinter\
            .Label(self.filename_frame)
        self.filename_error.pack(side=tkinter.LEFT)

        self.button_frame = tkinter.Frame(self, padx=10, pady=10)
        self.button_frame.pack(side=tkinter.BOTTOM)

        self.create_analysis_button = tkinter\
            .Button(self.button_frame, text="Create Analysis", state=tkinter.DISABLED, command=self.create_analysis)
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
        self.set_selector()

        if self.selector.validate_state():
            self.disable_non_selected()
            self.create_analysis_button.config(state=tkinter.NORMAL)
        else:
            self.enable_all_checks()
            self.create_analysis_button.config(state=tkinter.DISABLED)

    def set_selector(self):
        self.selector.recent_earnings = self.recent_earnings.get()
        self.selector.past_year_earnings = self.past_year_earnings.get()
        self.selector.pe_ratio = self.pe_ratio.get()
        self.selector.five_year_rev = self.five_year_rev.get()
        self.selector.five_year_earnings = self.five_year_earnings.get()
        self.selector.five_year_div = self.five_year_div.get()
        self.selector.div_yield = self.div_yield.get()
        self.selector.price_book = self.price_book.get()
        self.selector.price_sales = self.price_sales.get()
        self.selector.market_cap = self.market_cap.get()
        self.selector.volume = self.volume.get()
        self.selector.income = self.income.get()
        self.selector.roa = self.roa.get()
        self.selector.debt_equity = self.debt_equity.get()
        self.selector.profit = self.profit.get()

    def reset_checks(self):
        self.recent_earnings_check.deselect()
        self.past_year_earnings_check.deselect()
        self.pe_ratio_check.deselect()
        self.five_year_rev_check.deselect()
        self.five_year_earnings_check.deselect()
        self.five_year_div_check.deselect()
        self.div_yield_check.deselect()
        self.price_book_check.deselect()
        self.price_sales_check.deselect()
        self.market_cap_check.deselect()
        self.volume_check.deselect()
        self.income_check.deselect()
        self.roa_check.deselect()
        self.debt_equity_check.deselect()
        self.profit_check.deselect()

    def reset_analysis(self):
        self.enable_all_checks()
        self.reset_checks()
        self.filename_entry.delete(0, tkinter.END)
        self.filename_error.config(text="")
        self.create_analysis_button.config(state=tkinter.DISABLED)

    def validate_filename(self):
        filename = self.filename_entry.get()
        validator = FilenameValidator()
        valid = validator.validate(filename)

        if not valid:
            self.filename_error.config(text=validator.error_text)

        return valid

    def create_analysis(self):
        if self.validate_filename() and self.selector.validate_state():
            filename = f"{self.filename_entry.get()}.csv"
            data_collector = AnalysisDataCollector(self.selector)
            analysis_data = data_collector.get_analysis_data()
            aggregated_data = AnalysisDataAggregator(analysis_data)
            file_writer = AnalysisFilePrinter(aggregated_data)
            file_writer.write_file(filename)
            self.reset_analysis()
            messagebox.showinfo("Analysis Created", f"{filename} was created.")
