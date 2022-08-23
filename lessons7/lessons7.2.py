from abc import ABC, abstractmethod


class Сlothes(ABC):
    summ = 0

    def __init__(self, var):
        self.var = var

    @property
    @abstractmethod
    def summa(self):
        pass

    def __add__(self, other):
        Сlothes.summ += self.summa + other.summa
        return Costume(0)

    def __str__(self):
        text = Сlothes.summ
        Сlothes.summ = 0
        return f'{text}'


class Coat(Сlothes):
    @property
    def summa(self):
        return round(self.var / 6.5) + 0.5


class Costume(Сlothes):
    @property
    def summa(self):
        return round((2 * self.var + 0.3) / 100)


coat = Coat(24)
costume = Costume(34)

print(f' Общее необходимие количество ткани  - {coat + costume + coat} метров')
