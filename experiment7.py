from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Circle is drawn")

class Rectangle(Shape):
    def draw(self):
        print("Rectangle is drawn")

c = Circle()
r = Rectangle()

c.draw()
r.draw()