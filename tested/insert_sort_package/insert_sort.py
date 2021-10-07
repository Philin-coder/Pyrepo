def insertion_sort(ints: list) -> list:
    """
    Иллюстрация сортировки вставками
    :param ints: исходный список
    :return: отсортированный список
    >>> insertion_sort(ints=[1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1])
    [-6, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


    """
    if isinstance(ints, list) and all(isinstance(i, int) for i in ints):
        for i in range(1, len(ints)):
            temp = ints[i]
            j = i - 1
            while j >= 0 and temp < ints[j]:
                ints[j + 1] = ints[j]
                j = j - 1
            ints[j + 1] = temp
        return ints
    else:
        raise TypeError('Переданы неверные данне')
