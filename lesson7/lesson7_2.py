from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def calculation(self):
        pass


class coat(Wear):
    def calculation(self, v):
        self.v = v
        return v / 6.5 + 0.6


class suit(Wear):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0 and height < 3:
            self.__height = height
        else:
            self.__height = 0
            print("Error Height")

    def calculation(self):
        return 2 * self.__height + 0.3


c1 = coat()
print(c1.calculation(6.5))

s1 = suit(2)
print(s1.calculation())
