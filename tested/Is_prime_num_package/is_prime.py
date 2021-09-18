def is_prime_func(n: int) -> bool:
    """
    :param n: Целое число
    :return: Является ли оно простым(True-да, False=нет)
    >>> is_prime_func(n=2)
    True
    >>> is_prime_func(n=12)
    False

    """
    if isinstance(n, int):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n
    else:
        raise TypeError('введите целое число')


