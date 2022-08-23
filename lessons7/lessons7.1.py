class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.matrix]))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for r in range(len(other.matrix[i])):
                self.matrix[i][r] = self.matrix[i][r] + other.matrix[i][r]
            return Matrix.__str__(self)


matrix_1 = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
matrix_2 = Matrix([[8, 7], [6, 5], [4, 3], [2, 1]])


print(matrix_1.__add__(matrix_2))
