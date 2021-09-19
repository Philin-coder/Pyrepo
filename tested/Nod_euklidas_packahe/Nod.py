def gcd_func(a: int, b: int) -> int:
    """
    Нод 2 чисел по алгоритму Евклила
    :param a: первое число
    :param b: второе
    :return: Наибольший общий делитель этих чисел
    >>> gcd_func(a=12, b=2)
    2
    >>> gcd_func(a=2, b=5)
    1

    """
    if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
    else:
        raise TypeError('введите целые числа больше 0')
