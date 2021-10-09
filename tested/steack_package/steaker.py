def steak_area_func(x: int, y: int) -> str:
    """
    Попадает ли точка с координатами х и y в заштрихованную область
    :param x: координата точки по х
    :param y: координата точки по y
    :return: результат подсчета(попалает, или - нет, соответственно)
    >>> steak_area_func(x=12, y=11)
    'Нет'
    >>> steak_area_func(x=2, y=2)
    'Да'


    """
    if isinstance(x, int) and isinstance(y, int):
        if x >= 0 and x >= x - 6 and x * x + y * y <= 36:
            return 'Да'
        return 'Нет'
    else:
        raise TypeError('введены не числа')
