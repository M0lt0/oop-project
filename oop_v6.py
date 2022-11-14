# abstraction
from abc import ABC, abstractclassmethod


class Shape(ABC):

    abstractclassmethod

    def area(self):
        pass


@abstractclassmethod
def perimeter(self):
    pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class Rect(Shape):
    def __init__(self, l, w):
        self.__l = l
        self.__w = w

    def area(self):
        return self.__l * self.__w

    def perimeter(self):
        return (self.__l + self.__w) * 2


square = Square(15)
print(f"square area is {square.area()} and perimeter is {square.perimeter()}")
rect = Rect(15, 20)
print(f"square area is {rect.area()} and perimeter is {rect.perimeter()}")
