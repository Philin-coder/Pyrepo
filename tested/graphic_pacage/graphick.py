def graph(x: int, y: int) -> float:
    """
    :param x: коордианты по x
    :param y: коордианты по y
    :return:  при x=0 и y=-2 функция  (x ** 2) / 2) - 2 принимает значения
    >>> graph(x=0, y=-2)
    -2.0

    """
    if isinstance(x, int) or isinstance(y, int):
        if x == 0 and y == -2:
            return ((x ** 2) / 2) - 2
    else:
        raise TypeError('Введите целое число')
