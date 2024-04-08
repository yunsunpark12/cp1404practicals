from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        driven_distance = super().drive(distance)
        return driven_distance