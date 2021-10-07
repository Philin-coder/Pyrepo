def sel_sorting_func(ints: list) -> list:
    """
    Иллюстрация сортировки выбором
    :param ints: несортированный список
    :return:  несортированный список
    >>> sel_sorting_func(ints=[1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1])
    [-6, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    """
    if isinstance(ints, list) and all(isinstance(i, int) for i in ints):
        for i in range(len(ints) - 1):
            m = i
            j = i + 1
            while j < len(ints):
                if ints[j] < ints[m]:
                    m = j
                j = j + 1
                ints[i], ints[m] = ints[m], ints[i]

        return ints
    else:
        raise TypeError('Переданы неверые  данные')
