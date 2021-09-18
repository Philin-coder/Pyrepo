def maxim_func(a: int, b: int) -> int:
    """
    максимум, без использования if
    :param a: первое число
    :param b: второе число
    :return: максимум из них
    >>> maxim_func(a=1, b=2)
    2
    >>> maxim_func(a=0, b=1)
    1

    """
    if isinstance(a, int) or isinstance(b, int) or b == 0:
        try:
            c = a // b
            c = ((c + 2) // (c + 1)) % 2
            d = (c + 1) % 2
            return a * c + b * d
        except(TypeError, ZeroDivisionError):
            raise TypeError('введите 2 целых числа, b>0')
