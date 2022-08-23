class ComplexNum:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%x+%xj)' % (self.a, self.b)

    def __add__(self, other):
        numb_a = self.a + other.a
        numb_b = self.b + other.b
        return ComplexNum(numb_a, numb_b)

    def __mul__(self, other):
        numb_a = self.a * other.a - self.b * other.b
        numb_b = self.b * other.a + self.a * other.b
        return ComplexNum(numb_a, numb_b)


y1 = ComplexNum(5, 7)
y2 = ComplexNum(3, 9)

print(f"{y1} + {y2} =", y1 + y2)
print(f"{y1} * {y2} =", y1 * y2)
