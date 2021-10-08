def unique_list_func(work_list: list) -> list:
    """
    Фильтрация списка по критерию уникальности
    :param work_list: входящий список
    :return: отфильтрованный список
    >>> unique_list_func(work_list=[1, 2, 3, 3, 3, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> unique_list_func(work_list=['a', 'b', 'c', 'c', 'c', 'c', 'd', 'e'])
    ['a', 'b', 'c', 'd', 'e']
    >>> unique_list_func(work_list=[])
    []

    """
    ints = list()
    if isinstance(work_list, list):
        for i in work_list:
            if i not in ints:
                ints.append(i)
        return ints
    else:
        raise TypeError('передан не список')
