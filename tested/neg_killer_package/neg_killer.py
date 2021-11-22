def del_negs(n: int) -> list:
    """
    Удаление отрицательных.
    :param n:диапазон.
    :return:отфильтрованный список.
    >>> del_negs(n=12)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    """
    if isinstance(n, int):
        ints = [i for i in range(-100, n + 1)]
        return list(filter(lambda x: x > 0, ints))
    else:
        raise TypeError('передан неверный тип данных')
