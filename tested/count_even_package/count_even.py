def cnt_even(n: int) -> tuple:
    """
    :param n: количество элементов последовательности
    :return: количество четных элементов последовательности и нечетных соотвественно
    >>> cnt_even(12)
    [2, 4, 6, 8, 10]
    [1, 3, 5, 7, 9, 11]
    (6, ' ', 5)
    >>> cnt_even(13)
    [2, 4, 6, 8, 10, 12]
    [1, 3, 5, 7, 9, 11]
    (6, ' ', 6)
    >>> cnt_even(14)
    [2, 4, 6, 8, 10, 12]
    [1, 3, 5, 7, 9, 11, 13]
    (7, ' ', 6)

    """

    if isinstance(n, int):
        ints_even = [i for i in range(1, n) if not i % 2]
        print(ints_even)
        ints_odd = [i for i in range(1, n) if i % 2]
        print(ints_odd)
        return len(ints_odd), ' ', len(ints_even)
    else:
        raise TypeError('введите число')
