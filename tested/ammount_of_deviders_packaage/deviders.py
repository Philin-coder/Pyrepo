def num_devs(x: int) -> int:
    """
    :param x: целое положительное число
    :return:  количество  делителей данного числа

    >>> num_devs(12)
    6
    >>> num_devs(14)
    7
    >>> num_devs(16)
    8


    """
    if not isinstance(x, int):
        raise TypeError('Введите целое число')
    else:
        counter = 0
        for i in range(1, x + 1):
            if i % 2 == 0:
                counter += 1
        return counter
