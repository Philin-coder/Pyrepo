def get_max_sim(lst: list) -> int:
    """
    Простой поиск максимума.
    :param lst:исходный список.
    :return: максимум списка.
    >>> get_max_sim(lst=[1, 2, 3, 4])
    4
    """
    if isinstance(lst, list) and all(isinstance(i, int) for i in lst):
        mx = lst[0]
        for i in lst:
            if i > mx:
                mx = i

        return mx
    else:
        raise TypeError('передан неверный тип данных')
