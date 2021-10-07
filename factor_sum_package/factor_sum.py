def factor_sum_func(n: int) -> [int, tuple]:
    """
    Сумма факториалов интервала
    :param n:  диапазон
    :return: сумма его факториалов
    >>> factor_sum_func(n=10)
    1
    2
    6
    24
    120
    720
    5040
    40320
    362880
    3628800
    ('Sum: ', 1.7182818011463847)

    >>> factor_sum_func(n=11)
    1
    2
    6
    24
    120
    720
    5040
    40320
    362880
    3628800
    39916800
    ('Sum: ', 1.7182818261984931)

    """

    if isinstance(n, int):
        s = 0
        j = 1
        for i in range(1, n + 1):
            j *= i
            print(j)
            s += 1 / j
        return 'Sum: ', s
    else:
        raise TypeError('Введите целое число')


if __name__ == '__main__':
    print(factor_sum_func(n=10))
    # print(factor_sum_func(n='10'))
