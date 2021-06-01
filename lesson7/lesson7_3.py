class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __sub__(self, other):
        t = self.cell - other.cell
        return f'{t}' if t > 0 else 'error'

    def __truediv__(self, other):
        return round(self.cell / other.cell)

    def make_order(self, v):
        row = ''
        for i in range(int(self.cell // v)):
            row += '*' * v + '\n'
        row += '*' * (self.cell % v)
        return row


t1 = Cell(26)
t2 = Cell(13)
print(t1 + t2)
print(t1 * t2)
print(t1 - t2)
print(t1 / t2)
print(t2.make_order(5))
