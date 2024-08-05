from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

class square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


area_square = square(5)
print(area_square.area())

area_circle = Circle(2)
print(area_circle.area())

