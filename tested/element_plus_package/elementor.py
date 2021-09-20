def v_sum_func(n: int) -> list:
    """
    Поэлементное сложение векторов
    :param n: диапазон значений
    :return: результат поэлементного сложения векторов
    >>> v_sum_func(n=12)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]


    """
    if isinstance(n, int) and n >= 0:
        ints = [i for i in range(1, n + 1)]
        print(ints)
        ints1 = [i for i in range(1, n + 1)]
        print(ints1)
        return [i + j for i, j in zip(ints, ints1)] + (ints if len(ints) >= len(ints1) else ints1)[
                                                      min(len(ints), len(ints1)):]
    else:
        raise TypeError('Введите  целое положительное число')
