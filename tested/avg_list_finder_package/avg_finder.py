def avg_func(n: int) -> float:
    """
    поиск среднего значения диапазона
    :param n: диапазон значений
    :return: среднеее значение диапазона
    >>> avg_func(n=10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    5.5
    >>> avg_func(n=11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    6.0
    >>> avg_func(n=1)
    [1]
    1.0

    """
    if isinstance(n, int) and n > 0:
        ints = [i for i in range(1, n + 1)]
        print(ints)
        return sum(ints) / len(ints)
    else:
        raise TypeError('Введите целое положительное число больше 0')
