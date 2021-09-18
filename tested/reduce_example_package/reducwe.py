from functools import reduce


def red_func() -> list:
    """
    пример изменения списка
    :return: приобразованный функцией reduce список
    >>> red_func()
    1 2 3 4 5 6 7 8 9 10
    [4, 3, 2, 1]
    """
    ints = [i for i in range(1, 11)]
    print(*ints)
    return reduce(lambda res, i: [i] + res, [1, 2, 3, 4], [])

