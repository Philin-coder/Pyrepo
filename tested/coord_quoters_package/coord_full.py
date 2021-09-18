def coord_quoters(x: float, y: float) -> str:
    """
    В какой четверти находится точка
    :param x: координаты точки по x
    :param y: координаты точки по y
    :return: координатная четыверть, в которой нанходится точка
    >>> coord_quoters(x=10.0, y=10.0)
    'первая четврть'
    >>> coord_quoters(x=-10.0, y=10.0)
    'вторая четврть'
    >>> coord_quoters(x=-10.0, y=0.0)
    'третья четврть'
    >>> coord_quoters(x=11.0, y=-5.0)
    'четвертая четврть'


    """
    if isinstance(x, float) and isinstance(y, float):
        try:
            if (x > 0) and (y > 0):
                return 'первая четврть'
            if (x < 0) and (y > 0):
                return 'вторая четврть'
            if (x < 0) and (y <= 0):
                return 'третья четврть'
            if (x > 0) and (y < 0):
                return 'четвертая четврть'
        except TypeError:
            raise TypeError('Введите 2 вещественных числа')
    else:
        raise TypeError('Введите 2 вещественных числа')


