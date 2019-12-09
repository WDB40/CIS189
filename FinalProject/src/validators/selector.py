"""
Program: selector.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Used for keeping track of the factors selected and validating that only 5 were selected
"""


class Selector:
    def __init__(self):
        self.recent_earnings = False
        self.past_year_earnings = False
        self.pe_ratio = False
        self.five_year_rev = False
        self.five_year_earnings = False
        self.five_year_div = False
        self.div_yield = False
        self.price_book = False
        self.price_sales = False
        self.market_cap = False
        self.volume = False
        self.income = False
        self.roa = False
        self.debt_equity = False
        self.profit = False

    @property
    def recent_earnings(self):
        return self._recent_earnings

    @recent_earnings.setter
    def recent_earnings(self, value):
        self._recent_earnings = value

    @property
    def past_year_earnings(self):
        return self._past_year_earnings

    @past_year_earnings.setter
    def past_year_earnings(self, value):
        self._past_year_earnings = value

    @property
    def pe_ratio(self):
        return self._pe_ratio

    @pe_ratio.setter
    def pe_ratio(self, value):
        self._pe_ratio = value

    @property
    def five_year_rev(self):
        return self._five_year_rev

    @five_year_rev.setter
    def five_year_rev(self, value):
        self._five_year_rev = value

    @property
    def five_year_earnings(self):
        return self._five_year_earnings

    @five_year_earnings.setter
    def five_year_earnings(self, value):
        self._five_year_earnings = value

    @property
    def five_year_div(self):
        return self._five_year_div

    @five_year_div.setter
    def five_year_div(self, value):
        self._five_year_div = value

    @property
    def div_yield(self):
        return self._div_yield

    @div_yield.setter
    def div_yield(self, value):
        self._div_yield = value

    @property
    def price_book(self):
        return self._price_book

    @price_book.setter
    def price_book(self, value):
        self._price_book = value

    @property
    def price_sales(self):
        return self._price_sales

    @price_sales.setter
    def price_sales(self, value):
        self._price_sales = value

    @property
    def market_cap(self):
        return self._market_cap

    @market_cap.setter
    def market_cap(self, value):
        self._market_cap = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value):
        self._income = value

    @property
    def roa(self):
        return self._roa

    @roa.setter
    def roa(self, value):
        self._roa = value

    @property
    def debt_equity(self):
        return self._debt_equity

    @debt_equity.setter
    def debt_equity(self, value):
        self._debt_equity = value

    @property
    def profit(self):
        return self._profit

    @profit.setter
    def profit(self, value):
        self._profit = value

    def validate_state(self):
        count = 0
        if self.recent_earnings:
            count = count + 1
        if self.past_year_earnings:
            count = count + 1
        if self.pe_ratio:
            count = count + 1
        if self.five_year_rev:
            count = count + 1
        if self.five_year_earnings:
            count = count + 1
        if self.five_year_div:
            count = count + 1
        if self.div_yield:
            count = count + 1
        if self.price_book:
            count = count + 1
        if self.price_sales:
            count = count + 1
        if self.market_cap:
            count = count + 1
        if self.volume:
            count = count + 1
        if self.income:
            count = count + 1
        if self.roa:
            count = count + 1
        if self.debt_equity:
            count = count + 1
        if self.profit:
            count = count + 1

        if count == 5:
            return True
        else:
            return False
