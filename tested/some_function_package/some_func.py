def urg_func(x: float, y: float, xc: float, yc: float, r: float) -> str:
    """
    задан ург с центром
    :param x: координата точки по x
    :param y: координата точки по y
    :param xc:мнимые координаты точки
    :param yc:мнимые координаты точки
    :param r: радиус окружности
    :return: если точка покадает в круг, вернуть Yes, иначе NO
    >>> urg_func(x=1.0, y=2.0, xc=3.0, yc=4.0, r=5.0)
    'YES'
    >>> urg_func(x=-10.0, y=-10.0, xc=100.0, yc=-1.0, r=1.0)
    'NO'

    """
    if type(x).__name__ == 'float' or type(y).__name__ == 'float' or type(xc).__name__ == 'float' or type(
            yc).__name__ == 'float' or type(r).__name__ == 'float':
        res = (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r
        if res:
            return 'YES'
        else:
            return 'NO'
    else:
        raise TypeError('Введите веществвенное число')
