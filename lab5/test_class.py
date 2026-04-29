import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides

""" Позитивные тесты """

def test_equilateral():
    # Равносторонний треугольник: стороны 5,5,5
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == "equilateral"
    assert triangle.perimeter() == 15

def test_isosceles():
    # Равнобедренный треугольник: 5,5,8
    triangle = Triangle(5, 5, 8)
    assert triangle.triangle_type() == "isosceles"
    assert triangle.perimeter() == 18

def test_nonequilateral():
    # Разносторонний треугольник: 3,4,5
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"
    assert triangle.perimeter() == 12

def test_float_sides():
    # Равнобедренный треугольник с дробными сторонами: 2.5, 2.5, 3.0
    triangle = Triangle(2.5, 2.5, 3.0)
    assert triangle.triangle_type() == "isosceles"
    assert abs(triangle.perimeter() - 8.0) < 1e-9

def test_another_isosceles():
    # Другая комбинация равных сторон: 3,4,3
    triangle = Triangle(3, 4, 3)
    assert triangle.triangle_type() == "isosceles"


""" Негативные тесты (на создание объекта) """

def test_negative_side():
    # Отрицательная сторона: -1,2,3
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 2, 3)

def test_zero_side():
    # Нулевая сторона: 0,2,3
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 3)

def test_all_zero_sides():
    # Все стороны равны 0
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 0, 0)

def test_all_negative_sides():
    # Все стороны отрицательные: -1,-1,-1
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, -1, -1)

def test_inequality_equal():
    # Сумма двух сторон равна третьей: 1,2,3
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

def test_inequality_less():
    # Сумма двух сторон меньше третьей: 1,2,4
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 4)

def test_float_inequality():
    # Нарушение неравенства с float: 0.5,0.5,1.0
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0.5, 0.5, 1.0)

        