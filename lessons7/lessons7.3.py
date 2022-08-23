class Cell:
    def __init__(self, xxx):
        self.xxx = int(xxx)

    def __str__(self):
        return f'Результат операции {self.xxx * "*"}'

    def __add__(self, other):
        return Cell(self.xxx + other.xxx)

    def __sub__(self, other):
        return self.xxx - other.xxx if (self.xxx - other.xxx) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.xxx * other.xxx))

    def __truediv__(self, other):
        return Cell(round(self.xxx // other.xxx))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.xxx / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.xxx % cells_in_row)}'
        return row


cells1 = Cell(21)
cells2 = Cell(7)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(3))
print(cells1.make_order(7))
print(cells1 / cells2)