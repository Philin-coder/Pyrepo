def func(x: float, y: float, xc: float, yc: float, r: float) -> [float, str]:
    """
    находится ли точка в круге
    :param x: входной параметр
    :param y: входной параметр
    :param xc: входной параметр
    :param yc: входной параметр
    :param r: входной параметр
    :return: результат подсчета
    >>> func(x=1.0, y=1.0, xc=1.0, yc=1.0, r=1.0)
    'yes'
    >>> func(x=220.0, y=20.0, xc=2.0, yc=2.0, r=0.0)
    'No'

    """
    if isinstance(x, float) and isinstance(y,
                                           float) and isinstance(xc, float) and isinstance(yc, float) and isinstance(r,
                                                                                                                     float) or isinstance(
        x, int) and isinstance(y,
                               int) and isinstance(xc, int) and isinstance(yc, int) and isinstance(r, int):
        result = (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r
        if result:
            return 'yes'
        else:
            return 'No'
    else:
        raise TypeError('Введите вещественные числа')

