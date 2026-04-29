from triangle_func import IncorrectTriangleSides

class Triangle:
    def __init__(self, a, b, c):
        """ Инициализирует объект Triangle.
        Выбрасывает IncorrectTriangleSides, если стороны некорректны:
        не положительны, не удовлетворяют неравенству треугольника 
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides(
                "Стороны треугольника должны быть положительными числами"
            )

        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides(
                "Сумма любых двух сторон должна быть больше третьей"
            )

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        # Возвращает тип треугольника
        if self.a == self.b == self.c:
            return "equilateral"
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        return "nonequilateral"

    def perimeter(self):
        # Возвращает периметр треугольника
        return self.a + self.b + self.c
    

    