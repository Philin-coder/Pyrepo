def loop_back_func(n: int) -> list:
    """
    Демонстрация вывода в обратном порядке
    :param n: диапазон
    :return: список полученных значений
    >>> loop_back_func(n=12)
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    0
    [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    """
    if isinstance(n, int):
        ints = list()
        for i in reversed(range(n)):
            print(i)
            ints.append(i)
        return ints
    else:
        raise TypeError('Введите целое положительное число')
