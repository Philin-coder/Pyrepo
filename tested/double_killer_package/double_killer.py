def double_finder(repeated_sym: list) -> list:
    """
    Поиск  и подсчет дублей в списке
    :param repeated_sym: исходный список
    :return: отфильтрованный список
    >>> double_finder(repeated_sym=[1, 1, 2, 3, 3, 3, 4, 6])
    [1, 1, 2, 3, 3, 3, 4, 6]
    [1, 3]
    >>> double_finder(repeated_sym=['1', '1', '2'])
    ['1', '1', '2']
    ['1']
    >>> double_finder(repeated_sym=[])
    []
    []
    """
    if isinstance(repeated_sym, list):
        print(repeated_sym)
        doubles = list()
        for i in repeated_sym:
            if repeated_sym.count(i) > 1 and i not in doubles:
                doubles.append(i)
        return doubles
    else:
        raise TypeError('ВВеден не список')
