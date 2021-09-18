def row_sum_func(a: int, n: int) -> [int, float]:
    """
    сумма ряда при помощи цикла  for
    :param a: начальное значение
    :param n: шаг
    :return:  сумма ряда
     S = a/1 + a/2 + a/3 + ... a/n
    цикл for
    >>> row_sum_func(a=12, n=2)
    18.0
    >>> row_sum_func(a=34, n=12)
    105.50916305916307
    >>> row_sum_func(a=0, n=0)
    0

    """
    if isinstance(a, int) and isinstance(n, int):
        sun_r = 0
        for i in range(1, n + 1):
            sun_r += a / i
        return sun_r
    else:
        raise TypeError('Введите целые числа(диапазон и шаг)')
