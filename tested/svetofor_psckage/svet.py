def example(t1: int, t2: int, p: int, v: int, a: int) -> str:
    """
    :param t1: скорость на полосе, необходимая для смуляции работы светофора
    :param t2: скорость на полосе, необходимая для смуляции работы светофора
    :param p: скорость на полосе, необходимая для смуляции работы светофора
    :param v: скорость на полосе, необходимая для смуляции работы светофора
    :param a: скорость на полосе, необходимая для смуляции работы светофора
    :return: результат скорость движенич в км, либо сигнал пещеходу
    >>> example(30, 20, 145, 5, 3)
    'Pass'
    >>> example(10, 70, 200, 20, 4)
    '50.000 67.500'

    """
    if isinstance(t1, int) and isinstance(t2, int) and isinstance(p, int) and isinstance(v, int) and isinstance(a, int):
        if p / v % (t1 + t2) - t1 < 0:
            return "Pass"

        s = v ** 2 / (2 * a)
        t = t2 - (p - s) / v % (t1 + t2) + v / a
        return f"{s:.3f} {t:.3f}"
    else:
        raise TypeError('Введите число')
