def filter_func(n: int) -> list:
    """
    Пример работы с функцией filter
    :param n: число элементов последовательности
    :return:  отфтльтрованная последовательность(оставленны все элементы больше 5)
    >>> filter_func(n=12)
    1 2 3 4 5 6 7 8 9 10 11 12
    [6, 7, 8, 9, 10, 11, 12]
    >>> filter_func(n=4)
    1 2 3 4
    []
    >>> filter_func(n=5)
    1 2 3 4 5
    []



    """
    if isinstance(n, int):
        ints = [i for i in range(1, n + 1)]
        print(*ints)
        return list(filter(lambda i: i > 5, ints))
    else:
        raise TypeError('Введите количество элесентов последовательности(целое  число)')



