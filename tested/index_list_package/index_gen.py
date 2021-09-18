def mas_index_gen_func(n: int) -> dict:
    """
    Получение индекса элемента в списке
    :param n: длинна диапазна
    :return: словарь, где, ключ, это число, а значение -его индекс в списке
    >>> mas_index_gen_func(n=4)
    [1, 2, 3, 4]
    {1: 0, 2: 1, 3: 2, 4: 3}
    >>> mas_index_gen_func(n=15)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14}
    >>> mas_index_gen_func(n=0)
    []
    {}
    >>> mas_index_gen_func(n=-5)
    []
    {}

    """
    if isinstance(n, int):
        ints = [i for i in range(1, n + 1)]
        print(ints)
        indexes = [ints.index(i) for i in ints]
        return dict(zip(ints, indexes))
    else:
        raise TypeError('Введите целое число')


