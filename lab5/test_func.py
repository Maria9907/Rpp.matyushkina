import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunction(unittest.TestCase):
    """Тесты для функции get_triangle_type."""

    # Позитивные тесты

    def test_equilateral(self):
        # 1: равносторонний треугольник.
        self.assertEqual( get_triangle_type(3, 3, 3),"equilateral")

    def test_isosceles(self):
        # 2,4,5: равнобедренный треугольник
        self.assertEqual(get_triangle_type(3, 4, 3), "isosceles")
        self.assertEqual(get_triangle_type(5, 5, 8), "isosceles")
        self.assertEqual(get_triangle_type(2.5, 2.5, 3.0), "isosceles")

    def test_nonequilateral(self):
        # 3: разносторонний треугольник
        self.assertEqual(
            get_triangle_type(3, 4, 5),"nonequilateral")

    # Негативные тесты

    def test_inequality_raises(self):
        # 6: сумма двух равна третьей
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)
        # 7: сумма двух меньше третьей
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 4)
        # 12: float-случай
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0.5, 0.5, 1.0)

    def test_non_positive_sides_raises(self):
        """ Пункты 8, 9, 10, 11: нулевые и отрицательные стороны """
        # 8: одна отрицательная
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)
        # 9: одна нулевая
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 3)
        # 10: все нули
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)
        # 11: все отрицательные
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, -1, -1)

if __name__ == '__main__':
    unittest.main() 

