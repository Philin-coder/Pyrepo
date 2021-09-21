import math


def m_gcd_func(a: int, b: int) -> int:
    """
    Алгоритм нахождения  НОК(с исполбзованием math.gcd)
    :param a:  целое число
    :param b: второе целое число
    :return: НОК(Наименьшее общее кратное данных чисел)
    >>> m_gcd_func(a=14, b=21)
    42

    """
    if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0:
        return (a * b) // math.gcd(a, b)
    else:
        raise TypeError('Введите 2 целых подложительных числа')
