from prac_9.guitar import Guitar
from prac_9.musician import Musician


class Band:
    def __init__(self, name,):
        self.name = name        self.members = []

    def __str__(self):
        return f'{self.name} ({self.members[0]}, {self.members[1]}, {self.members[2]}, {self.members[3]})'

    def add(self, member):
        self.members.append(member)

    def play(self):
        for number in range(4):
            print(Musician.play(self.members[number]))