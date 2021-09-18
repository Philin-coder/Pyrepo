def deleter() -> list:
    """
    удаление повторяющихся значений из списка
    :return: результирующий список
    >>> deleter()
    [50, '0032', 765]

    """
    if isinstance([50, '0032', 17, 25, 765, 217, 25, 217, 17], list):
        any_list = [50, '0032', 17, 25, 765, 217, 25, 217, 17]
        return [i for i in any_list if any_list.count(i) == 1]
    else:
        raise TypeError('Подано значение неверного типа')
