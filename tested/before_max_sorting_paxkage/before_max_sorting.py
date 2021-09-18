def max_sort_gen_func(ints: list) -> list:
    """
    Сортировка по возрастанию перед максимумом
    :param ints: список целых чисел
    :return:список отсортированных(по возрастанию, перед максимумом)
    >>> max_sort_gen_func(ints=[2, 3, 4, 1, 10, 12])
    [1, 2, 3, 4, 10, 12]

    """

    if isinstance(ints, list) and  all(isinstance(i,int) for i in ints):
        return sorted(ints[:ints.index(max(ints))]) + ints[ints.index(max(ints)):]
    else:
        raise TypeError('Введите список  чисел')


