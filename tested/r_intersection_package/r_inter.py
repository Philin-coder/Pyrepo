import math


def r_intersection(r: float, a: float, b: float) -> [str, tuple]:
    """
    Задана окружность с центром в точке O(0, 0) и радиусом R0 и прямая
    y = ax+b. Определить, пересекаются ли прямая и окружность. Если пере-
    секаются, найти точки пересечения


    :param r: радиус окружности (вещественное число)
    :param a: начало прямой
    :param b: конец прямой
    :return: если прямоя и окружность пересекаются, выводятся точки, в которых происходит пересечение
    >>> r_intersection(r=1.0, a=2.0, b=3.4)
    'Прямая и окружность не пересекаются'
    >>> r_intersection(r=0.0, a=0.0, b=0.0)
    ('Прямая касается окружности в точке', -0.0, 0.0)

    >>> r_intersection(r=1.0, a=2.0, b=0.0)
    ('Прямая пересекает окружность в точках:', 0.447, 0.894, -0.447, -0.894)

    """
    if isinstance(r, float) or isinstance(a, float) or isinstance(b, float):
        a1 = a * a + 1
        b1 = 2 * a * b
        c1 = b * b - r * r
        d = b1 * b1 - 4 * a1 * c1
        if d < 0:
            return 'Прямая и окружность не пересекаются'
        elif d == 0:
            x1 = -b1 / (2 * a1)
            y1 = a * x1 + b
            return 'Прямая касается окружности в точке', float(f'{x1:.3f}'), float(f'{y1:.3f}')
        else:
            x1 = (-b1 + math.sqrt(d)) / (2 * a1)
            x2 = (-b1 - math.sqrt(d)) / (2 * a1)
            y1 = a * x1 + b
            y2 = a * x2 + b
            return 'Прямая пересекает окружность в точках:', float(f'{x1:.3f}'), float(f'{y1:.3f}'), float(
                f'{x2:.3f}'), float(f'{y2:.3f}')
    else:
        raise TypeError('Введите вещественное число')
