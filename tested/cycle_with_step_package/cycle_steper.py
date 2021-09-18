def cycle_step(a: int, b: int, step: int) -> list:
    """
    Иллюстрация работы цикла с шагом
    :param a: начало диапазона
    :param b:  конец
    :param step: шаг
    :return: список полцченных значений
    >>> cycle_step(a=1, b=8, step=2)
    [1, 3, 5, 7]
    >>> cycle_step(a=1, b=8, step=1)
    [1, 2, 3, 4, 5, 6, 7]
    >>> cycle_step(a=-10, b=10, step=1)
    [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
    if isinstance(a, int) and isinstance(b, int) and isinstance(step, int) and a != 0 and b != 0 and step != 0:
        ints = [i for i in range(a, b, step)]
        return ints
    else:
        raise TypeError('Введите 3 целых положительных числа(начало диапазрна, конец диапазона и шаг )')
