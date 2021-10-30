def how_many_hour_and_minutes(n: int) -> [int, tuple]:
    """
    количество часов и минут в количестве минут.
    :param n: количество минут(148)
    :return: количество часов и минут(2,28)
    >>> how_many_hour_and_minutes(n=148)
    (2, 28)

    """
    if isinstance(n, int) and n > 0:
        h = n // 60
        if h >= 24:
            return h % 24, n % 60
        else:
            return h, n % 60
    else:
        raise TypeError('Введите целое положительное число')
