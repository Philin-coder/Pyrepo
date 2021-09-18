import math


def nod(a: int, b: int) -> int:
    """
    :param a: целое число
    :param b: второе целое число
    :return: Наибоольший Общий Делитель этих чисел
    >>> nod(a=12, b=128)
    4
    >>> nod(a=11, b=121)
    11
    >>> nod(a=14, b=500)
    2

    """
    if isinstance(a, int) and isinstance(b, int):
        return math.gcd(a, b)
    else:
        raise TypeError('Введите целое число')
