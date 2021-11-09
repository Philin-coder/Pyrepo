def tuple_gen_func(start_p: int, end_p: int) -> tuple:
    """
    превращение картежа во множество.
    :param start_p: начало диапазона .
    :param end_p: конец диапазона .
    :return: set из 2-х картежей в диапазоне от start_p до end_p
    >>> tuple_gen_func(start_p=1, end_p=4)
    (1, 2, 3, 4)
    """
    if (start_p, int) and isinstance(end_p, int):
        return tuple([i for i in range(start_p, end_p + 1)])
    else:
        raise TypeError('Передан неверный тип данных')


def tuple_merger(t1: tuple, t2: tuple) -> set:
    """
    Слияния кортежей.
    :param t1: кортеж 1
    :param t2: второй.
    :return: результат(set)
    >>> tuple_merger(t1=tuple_gen_func(start_p=1, end_p=4), t2=tuple_gen_func(start_p=5, end_p=8))
    {(1, 2, 3, 4), (5, 6, 7, 8)}

    """
    res = set()
    if isinstance(res, set) and len(res) == 0:
        res.add(t1)
        res.add(t2)
        return res
    else:
        raise TypeError('Передан неверный тип данных, либо непустое множество')
