def min_in_mas(n: int) -> int:
    """
    >>> min_in_mas(n=10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    1
    >>> min_in_mas(n=3)
    [1, 2, 3]
    1

    Нахождение минимума(встроенными функциями)
    :param n: диапазон значений
    :return: минимум в диапазоне
    """
    if isinstance(n, int) and n != 0 and n > 0:
        ints = [i for i in range(1, n + 1)]
        print(ints)
        return min(ints)
    else:
        raise TypeError('Введите число положительное , не равное 0')


