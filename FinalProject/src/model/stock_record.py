class StockRecord:
    def __init__(self, ticker, name, last_price):
        self.ticker = ticker
        self.name = name
        self.last_price = last_price

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        self._ticker = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_price(self):
        return self._last_price

    @last_price.setter
    def last_price(self, value):
        self._last_price = value

    def __str__(self):
        return f"StockRecord[Ticker: {self.ticker}; Name: {self.name}; Last Price: {self.last_price}]"
