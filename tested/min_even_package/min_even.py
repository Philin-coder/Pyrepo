def min_evan_func(start_step: int, n: int) -> [int, str]:
    """

    :param start_step: начало диапазона
    :param n: конец диапазона
    :return: минимум(четный), диапазона
    >>> min_evan_func(start_step=2, n=8)
    [2, 3, 4, 5, 6, 7, 8]
    2
    >>> min_evan_func(start_step=1, n=10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    'минимум не четный,он равен 1'
    >>> min_evan_func(start_step=0, n=0)
    [0]
    0

    """
    if isinstance(start_step, int) and isinstance(n, int):
        try:
            ints = [i for i in range(start_step, n + 1)]
            print(ints)
            if min(ints) % 2 == 0:
                return min(ints)
            else:
                return f'минимум не четный,он равен {min(ints)}'
        except TypeError:
            raise TypeError('введите 2 целых числа(начало и конец диапазона)')
    else:
        raise TypeError('введите 2 целых числа(начало и конец диапазона)')


