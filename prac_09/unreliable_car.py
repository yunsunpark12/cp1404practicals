from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    def __int__(self, reliability, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= random_number:
            super().drive(0)
        return distance