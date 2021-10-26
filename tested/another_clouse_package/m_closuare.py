def multiplier(n: int) -> [int, float]:
    """
    Замыкание
    :param n: множитель
    :return: произведение
    >>> mul2 = multiplier(n=2)
    >>> mul2(5)
    10
    """

    if isinstance(n, int):
        def mul(k: int) -> [int, float]:
            if isinstance(k, int):
                return n * k

        return mul
    else:
        raise TypeError('Введите числа')
