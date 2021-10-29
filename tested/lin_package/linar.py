import itertools


def lin_list(vals: list) -> list:
    """
    Линаризация списка
    :param vals: исходный список
    :return: результирующий  список
    >>> lin_list(vals=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> lin_list(vals=[[1, 2, 3], [4, 5, 6], [7, 8, 9, 'f']])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 'f']


    """
    if isinstance(vals, list):
        return list(itertools.chain(*vals))
    else:
        raise TypeError('передан неверный тип данных')
