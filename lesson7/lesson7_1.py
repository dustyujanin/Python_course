class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(item) for item in i]) for i in self.matrix]))

    def __add__(self, other):
        matrix_sum = []
        for i in range(len(self.matrix)):
            row_list = []
            for j in range(len(self.matrix[i])):
                row_list.append(self.matrix[i][j] + other.matrix[i][j])
            matrix_sum.append(row_list)
        return matrix_sum


m1 = Matrix([[1, 2], [3, 4],[5,6]])
m2 = Matrix([[7, 8], [9, 10],[11,12]])
print('Матрица 1')
print(m1)
print('\nМатрица 2')
print(m2)
print('\nСумма матриц')
print(m1 + m2)
