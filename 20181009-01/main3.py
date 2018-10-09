class Person:
    name = None
    height = None
    weight = None
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

p1 = Person("Joe", 175, 75)
print(p1.name, ":", p1.bmi())