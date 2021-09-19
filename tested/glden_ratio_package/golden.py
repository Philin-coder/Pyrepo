def golden_ratio_func(gr: int) -> [int, float]:
    """
    Золотое сечене числа
    :param gr: число
    :return:и его золотое сечене
    >>> golden_ratio_func(gr=12)
    0.38197424892703863
    >>> golden_ratio_func(gr=9)
    0.38181818181818183

    """
    if isinstance(gr, int):
        b1 = 0
        a, b = 0, 1
        cnt = 1
        while cnt <= gr:
            a, b = b, a + b
            cnt += 1
            if cnt == (gr - 1):
                b1 = b
        return b1 / b
    else:
        raise TypeError('Введите число')
