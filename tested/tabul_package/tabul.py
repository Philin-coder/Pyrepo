def tab_func(dx: float) -> list:
    """
    Пример табулирования
    :param dx:шаг
    :return: печатается таблица значений функции
    >>> tab_func(dx=0.25)
    0.0
    0.00390625
    0.0625
    0.31640625
    1.0
    2.44140625
    5.0625
    9.37890625
    16.0
    25.62890625
    [0.0, 0.00390625, 0.0625, 0.31640625, 1.0, 2.44140625, 5.0625, 9.37890625, 16.0, 25.62890625]
    >>> tab_func(dx=25)
    0
    390625
    [0, 390625]


    """
    floats = list()
    if isinstance(dx, float) or isinstance(dx, int):
        x = -dx
        while x <= 2:
            x = x + dx
            y = x ** 4
            print(y)
            floats.append(y)
        return floats
    else:
        raise TypeError('Введено не   число')
