"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import ABC

class IPlayer(ABC):

    def hp(self):
        raise NotImplementedError

    def name(self):
        raise NotImplementedError

class Player(IPlayer):
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: IPlayer):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
