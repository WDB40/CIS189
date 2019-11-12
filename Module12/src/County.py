def clean_dollar_formatting(value):
    return float(str(value).strip('$').strip(" ").replace(',', ''))


class County:
    def __init__(self, name, rank, per_capita, household_income, family_income, population, num_households):
        self.name = name
        self.rank = rank
        self.per_capita = per_capita
        self.household_income = household_income
        self.family_income = family_income
        self.population = population
        self.num_households = num_households

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value == "":
            raise TypeError
        else:
            self._rank = value

    @property
    def per_capita(self):
        return self._per_capita

    @per_capita.setter
    def per_capita(self, value):
        self._per_capita = clean_dollar_formatting(value)

    @property
    def household_income(self):
        return self._household_income

    @household_income.setter
    def household_income(self, value):
        self._household_income = clean_dollar_formatting(value)

    @property
    def family_income(self):
        return self._family_income

    @family_income.setter
    def family_income(self, value):
        self._family_income = clean_dollar_formatting(value)

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = clean_dollar_formatting(value)

    @property
    def num_households(self):
        return self._num_households

    @num_households.setter
    def num_households(self, value):
        self._num_households = clean_dollar_formatting(value)

    def __str__(self) -> str:
        return f"County[Name: {self.name}; Rank: {self.rank}; Per Capita: {self.per_capita}; Household Income: {self.household_income}; Family Income: {self.family_income}; Population: {self.population}; Number of Households: {self.num_households};]"

    def __repr__(self) -> str:
        return self.__str__()
