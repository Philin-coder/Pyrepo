def dig_root_func(n: int) -> int:
    """
    Цифровой корень натурального числа получается следующим образом.
    Складываются все цифры данного числа.
    Процесс повторяется, пока в результате не будет получено однозначное число,
    которое и называется цифровым корнем числа.
    :param n: целое число
    :return:числовой коронь числа
    >>> dig_root_func(n=12)
    3
    >>> dig_root_func(n=0)
    0
    >>> dig_root_func(n=1123)
    7

    """
    if isinstance(n, int) and not isinstance(n, float):
        fend = False
        s = 0
        while not fend:
            s += n % 10
            n = n // 10
            if n == 0:
                if s < 10:
                    fend = True
                else:
                    n = s
                    s = 0

        return s

    else:
        raise TypeError('Введите число')
