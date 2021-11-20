def max_end_min(n: int) -> tuple:
    """
    Отыскание максимума и минимума на диапазона
    :param n: начало диапазона.
    :return: максимум и минимум.
    >>> max_end_min(n=6)
    [1, 2, 3, 4, 5, 6]
    (6, 1)
    """

    if isinstance(n, int) and n > 0:
        ints = [i for i in range(1, n + 1)]
        print(ints)
        return max(ints), min(ints)
    else:
        raise TypeError('Передан неверный тип данных, либо - неверное значение диапазона')
