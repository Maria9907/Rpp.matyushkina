class IncorrectTriangleSides(Exception):
    # Исключение, выбрасываемое при некорректных сторонах треугольника
    pass

def get_triangle_type(a, b, c):
    # Стороны должны быть положительными
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны должны быть положительными числами.")

    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Не выполняется неравенство треугольника.")

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"
    

    