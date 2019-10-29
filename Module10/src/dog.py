class Dog:
    @property
    def breed(self):
        return self._breed

    @property
    def weight(self):
        return self._weight

    @property
    def color(self):
        return self._color

    @property
    def gender(self):
        return self._gender

    @breed.setter
    def breed(self, value):
        self._breed = value

    @color.setter
    def color(self, value):
        self._color = value

    @weight.setter
    def weight(self, value):
        self._weight = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    def __init__(self, breed="lab", weight=50, color="chocolate", gender="female"):
        self._breed = breed
        self._weight = weight
        self._color = color
        self._gender = gender

    def bark(self):
        print("Woof!")

    def sit(self):
        if self.gender == "female":
            print("Good, girl!")
        elif self.gender == "male":
            print("Good, boy!")

    def __str__(self) -> str:
        return "The dog - breed: " + self.breed + "; weight: " + str(self.weight) + "; color: " + self.color + "; gender: " + self.gender


