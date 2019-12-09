"""
Program: ranking_record.py
Author: Wes Brown
Last date modified: 12/08/19

Purpose: Used for storing information each factor for each stock - each factor has one of these so 15 per stock
"""


class RankingRecord:
    def __init__(self, ticker, factor, rank):
        self.ticker = ticker
        self.factor = factor
        self.rank = rank

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        self._ticker = value

    @property
    def factor(self):
        return self._factor

    @factor.setter
    def factor(self, value):
        self._factor = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    def __str__(self):
        return f"RankingRecord[Ticker: {self.ticker}; Factor Value: {self.factor}; Factor Rank: {self.rank}"
