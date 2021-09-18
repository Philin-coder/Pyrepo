def sorting_mas_func(mixed_list: list) -> list:
    """
    Сортировка списка,масимум впереди
    :param mixed_list: неотсортированный список от большего к меньшему
    :return: отсортированный список
    >>> sorting_mas_func(mixed_list=[4, 8, 2])
    [8, 4, 2]
    >>> sorting_mas_func(mixed_list=[1, 2, 3])
    [3, 1, 2]
    >>> sorting_mas_func(mixed_list=[3, 1, 6])
    [6, 3, 1]

    """
    if isinstance(mixed_list, list) and all(isinstance(i, int) for i in mixed_list):
        mx = mixed_list[0]
        for i in mixed_list:
            if mx < i:
                mx = i
        m_id = mixed_list.index(mx)
        del mixed_list[m_id]
        return [mx] + mixed_list
    else:
        raise TypeError('Получен не список цифр')
