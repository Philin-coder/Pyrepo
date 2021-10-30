def lean_rec(lst: list) -> list:
    """
    Линаризация списка рекурсивно.
    :param lst: исходный список.
    :return: результирующий список
    >>> lean_rec(lst=[[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]])
    [1, 2, 4, 2, 4, 8, -4, 'er', 0, {2: 'primer'}]
    """
    if isinstance(lst, list):
        rec_lst = []
        for a in lst:
            if type(a) == list:
                rec_lst += lean_rec(a)
            else:
                rec_lst += [a]
        return rec_lst
    else:
        raise TypeError('Передан неверный тип данных')
