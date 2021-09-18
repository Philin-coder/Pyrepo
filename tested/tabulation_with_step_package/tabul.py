def tab_func(dx: float, x: int) -> list:
    """
    Табулирование с шагом
    :param dx:   шаг табуляции
    :param x: количество чисел
    :return: список чисел
    >>> tab_func(dx=1.1, x=2)
    3.0
    4.21
    7.840000000000001
    [3.0, 4.21, 7.840000000000001]


    >>> tab_func(dx=10, x=1)
    3
    103
    [3, 103]
    >>> tab_func(dx=100, x=12)
    3
    10003
    [3, 10003]

    """
    if isinstance(x, int) and isinstance(dx, float) or isinstance(dx, int) and not isinstance(x, str):
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
