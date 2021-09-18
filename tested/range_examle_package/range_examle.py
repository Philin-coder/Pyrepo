def range_func(a: int, b: int) -> list:
    """
    Возврат списка чисел в диапазоне,
    :param a: начало списка
    :param b: конец списка
    :return: собственно, список
    >>> range_func(1, 8)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> range_func(0, 0)
    [0]
    >>> range_func(1, 11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


    """
    if isinstance(a, int) and isinstance(b, int):
        return list(range(a, b + 1))
    else:
        raise TypeError('Должны быть введенв 2 целых числа не равных 0')
