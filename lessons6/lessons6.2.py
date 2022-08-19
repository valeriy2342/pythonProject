class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        self.thickness = 5

    def summ(self):
        x = self._length * self._width * self.mass * self.thickness / 1000
        print(f'Требуется {(round(x))} тон асфальта')


r = Road(5000, 20)
r.summ()
