def half_list_gen_func(n: int) -> [list, tuple]:
    """
    Получение половин сприска
    :param n: диапазон
    :return:половины списка(картеж)
    >>> half_list_gen_func(n=10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ([6, 7, 8, 9, 10], [1, 2, 3, 4, 5])

    """
    start_list = [i for i in range(1, n + 1)]
    if isinstance(n, int) and any(isinstance(i, int) for i in start_list):
        try:
            print(start_list)
            return start_list[n // 2:], start_list[:n // 2]
        except TypeError:
            raise TypeError('передан неверный тип даны]')
    else:
        raise TypeError('can only concatenate str (not "int") to str')
