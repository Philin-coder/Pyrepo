def coordinate_quoters(x: float, y: float) -> bool:
    """
    Правда ли, что точки с координатами x и y находится в одной из координатнных четветей(1 или второйй)
    coordinate_quoters(0.0, 0.0) - по условию не возможно, так как точка, тогда не находится в какой-либо из четвертей
    :param x: координата точки x
    :param y: координата точки y
    :return: True, либо falss в зависимости от координатнат точки
    >>> coordinate_quoters(3, 4)
    True
    >>> coordinate_quoters(-3.5, 8)
    True
    >>> coordinate_quoters(0.0, 0.0)


    """
    if isinstance(x, float) or isinstance(y, float) or isinstance(x, int) or isinstance(x, int):
        try:
            if (x > 0) and (y > 0):
                return True
            if (x < 0) and (y > 0):
                return True
        except TypeError:
            raise TypeError('Должны быть введены числа, целые, либо вещественные')
    else:
        raise TypeError('Должны быть введены числа, целые, либо вещественные')
