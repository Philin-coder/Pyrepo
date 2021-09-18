def set_gen() -> list:
    """
    Отбор уникальых чисел в списке
    :return: уникальыне числа в списке
    >>> set_gen()
    1 2 2 3 4 5
    [1, 2, 3, 4, 5]
    """

    ints = (1, 2, 2, 3, 4, 5)
    print(*ints)
    return list(set(ints))
