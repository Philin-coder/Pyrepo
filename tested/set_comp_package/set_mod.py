def set_analyser_func(a: int, b: int, c: int) -> int:
    """
    Иллюстрация работы с set
    :param a: числовая переменная
    :param b: числовая переменная
    :param c: числовая переменная
    :return: если число уникально, то от числа  4 отнимается длинна set, то есть -количество уникальных числел,
    при k=1(уникаотные  числа все) вернет  0
    иначе вернет количество одинаковых чисеk
    >>> set_analyser_func(a=1, b=1, c=1)
    3
    >>> set_analyser_func(a=5, b=8, c=1)
    0

    """
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        k = 4 - len({a, b, c})
        if k == 1:
            k = 0
        return k
    else:
        raise TypeError('передан неправильный тип данных')


