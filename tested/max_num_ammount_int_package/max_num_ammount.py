def num_div(n: int) -> int:
    """
    Количество(максимальное) делителей на интервале.
    :param n: диапазон.
    :return: количество.
    >>> num_div(n=12)
    6
    """
    if isinstance(n, int):
        r = 2
        i = 2
        while i * i <= n:
            if n % i == 0:
                r += 1
            if n // i != i:
                r += 1
            i += 1
        return r
    else:
        raise TypeError('Передан неправильный тип данных')


def mx_finder(a: int, b: int) -> int:
    """
    Максимум на интервале
    :param a: начало интервала.
    :param b: конец интервала.
    :return: максимум.
    >>> mx_finder(a=1, b=128)
    120
    """
    x_max = 0
    d_max = 0
    if isinstance(a, int) and isinstance(b, int):
        x = b
        while x >= a:
            nd = num_div(x)
            if nd > d_max:
                d_max = nd
                x_max = x
            x -= 1
        return x_max
    raise TypeError('Передан неправильный тип данных')
