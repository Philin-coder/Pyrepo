import math


def dif_func(a: float, e: float) -> float:
    """
    Демонстрация решения дифференцциального уровнения
    :param a: входной параметр
    :param e: входной параметр
    :return: результат
    >>> dif_func(a=12.3, e=12.3)
    (-5.983353400899203e-14+325.7185884161348j)

    """
    if isinstance(a, float) and isinstance(e, float):
        f = 6.672 * 10 ** -12
        m = 5.9737 * 10 ** 24
        v = 0
        return ((1 + e * math.cos(v)) ** 2) / ((1 - (e ** 2)) ** (3 / 2)) * (math.sqrt(f * m) / a ** 3)
    else:
        raise TypeError('Введите 2 вещественных числа')
