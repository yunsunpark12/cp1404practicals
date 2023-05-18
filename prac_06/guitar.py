class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        this_year = 2022
        if "L-5" in self.name:
            self.year = 1922
        age = this_year - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return "(vintage)"
        else:
            return False