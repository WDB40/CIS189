class AnalysisRecord:
    def __init__(self):
        self.ticker = ""
        self.average_rank = ""
        self.factor_one = ""
        self.rank_one = ""
        self.factor_two = ""
        self.rank_two = ""
        self.factor_three = ""
        self.rank_three = ""
        self.factor_four = ""
        self.rank_four = ""
        self.factor_five = ""
        self.rank_five = ""

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        self._ticker = value

    @property
    def factor_one(self):
        return self._factor_one

    @factor_one.setter
    def factor_one(self, value):
        self._factor_one = value

    @property
    def rank_one(self):
        return self._rank_one

    @rank_one.setter
    def rank_one(self, value):
        self._rank_one = value

    @property
    def factor_two(self):
        return self._factor_two

    @factor_two.setter
    def factor_two(self, value):
        self._factor_two = value

    @property
    def rank_two(self):
        return self._rank_two

    @rank_two.setter
    def rank_two(self, value):
        self._rank_two = value

    @property
    def factor_three(self):
        return self._factor_three

    @factor_three.setter
    def factor_three(self, value):
        self._factor_three = value

    @property
    def rank_three(self):
        return self._rank_three

    @rank_three.setter
    def rank_three(self, value):
        self._rank_three = value

    @property
    def factor_four(self):
        return self._factor_four

    @factor_four.setter
    def factor_four(self, value):
        self._factor_four = value

    @property
    def rank_four(self):
        return self._rank_four

    @rank_four.setter
    def rank_four(self, value):
        self._rank_four = value

    @property
    def factor_five(self):
        return self._factor_five

    @factor_five.setter
    def factor_five(self, value):
        self._factor_five = value

    @property
    def rank_five(self):
        return self._rank_five

    @rank_five.setter
    def rank_five(self, value):
        self._rank_five = value

    @property
    def average_rank(self):
        return self._average_rank

    @average_rank.setter
    def average_rank(self, value):
        self._average_rank = value
