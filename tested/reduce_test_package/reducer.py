from functools import reduce


def multer_reduce_func(n: int) -> int:
    """
    произведенеи списка
    :param n: целое списка
    :return: произведением списка
    >>> multer_reduce_func(n=10)
    1 2 3 4 5 6 7 8 9 10
    3628800
    >>> multer_reduce_func(n=20)
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    2432902008176640000
    >>> multer_reduce_func(n=1)
    1
    1
    """
    if isinstance(n, int):
        ints = [i for i in range(1, n + 1)]
        print(*ints)
        return reduce(lambda m, i: m * i, ints, 1)
    else:
        raise TypeError('Введите число')
