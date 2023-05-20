import math


class Figure:
    def __init__(self):
        pass

    def get_square(self):
        pass

    def get_perimeter(self):
        pass


class Triangle(Figure):
    def __init__(self, base, height, third_side):
        super().__init__()
        self.base = base
        self.height = height
        self.third_side = third_side

    def get_square(self):
        print(0.5 * self.base * self.height)

    def get_perimeter(self):
        print(self.base + self.height +self.third_side)


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_square(self):
        print(math.pi * self.radius ** 2)

    def get_perimeter(self):
        print(2 * math.pi * self.radius)


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def get_square(self):
        print(self.length * self.width)

    def get_perimeter(self):
        print(2 * (self.length + self.width))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

