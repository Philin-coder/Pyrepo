class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        return 0

    def print_area(self):
        print(f'Фигура: {self.name}; площадь: {self.get_area()}')


class Rectangle(Figure):
    """Прямоугольник. Конструктор принимает длину и ширину"""

    def __init__(self, a, b):
        self.a, self.b = a, b
        super().__init__('прямоугольник')

    def get_area(self):
        return self.a * self.b


class RightTriangle(Figure):
    """Прямоугольный треугольник. Конструктор принимает длины катетов"""

    def __init__(self, leg_1, leg_2):
        self.leg_1, self.leg_2 = leg_1, leg_2
        super().__init__('прямоугольный треугольник')

    def get_area(self):
        return self.leg_1 * self.leg_2 / 2


class Circle(Figure):
    """Круг. Конструктор принимает радиус"""

    def __init__(self, radius):
        self.radius = radius
        super().__init__('круг')

    def get_area(self):
        return 3.14 * self.radius * self.radius


r = Rectangle(20, 40)
r.print_area()
c = Circle(20)
c.print_area()
tr = RightTriangle(30, 40)
tr.print_area()
