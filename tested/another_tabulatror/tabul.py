def tab_func(x: int) -> list:
    """
    Пример табулирования
    :param x:гранницы табулирования
    :return: список значений функции
    >>> tab_func(x=10)
    3.0
    7.0
    19.0
    39.0
    67.0
    103.0
    147.0
    [3.0, 7.0, 19.0, 39.0, 67.0, 103.0, 147.0]
    >>> tab_func(x=-1)
    3.0
    [3.0]
    >>> tab_func(x=1)
    3.0
    7.0
    [3.0, 7.0]

    """
    if isinstance(x, int):
        dx = 2.0
        step_t = -dx
        floats = list()
        while step_t <= x:
            step_t += dx
            y = step_t ** 2 + 3
            print(y)
            floats.append(y)
        return floats
    else:
        raise TypeError('Введите число')
