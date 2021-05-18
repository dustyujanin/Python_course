class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length
        self.weight = 25
        self.height = 5

    def calculate(self):
        print(self._length * self._width * self.height * self.weight)


a = Road(2, 1)
a.calculate()
