class Guitar:
    def __init__(self, name="", year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}". format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2018 - self.year
        return age

    def is_vintage(self):
        if int(self.get_age()) > 50:
            return True
        else:
            return False


if __name__ == "__main__":

    g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(g1.get_age())
    print(g1.is_vintage())
