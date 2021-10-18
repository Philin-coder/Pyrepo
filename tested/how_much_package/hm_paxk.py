def word_counter(w_let: str, rep_pvt: int) -> [int, tuple]:
    """
    Максимум слов из букв больше k
    :param w_let:текстовая  строка
    :param rep_pvt: количество букв
    :return: количество слов
    >>> word_counter(w_let='мир', rep_pvt=2)
    мм
    ми
    мр
    им
    ии
    ир
    рм
    ри
    рр
    ('итого', 9)


    """
    if isinstance(w_let, str) and isinstance(rep_pvt, int) and rep_pvt >= 0:
        pools = [tuple(pool) for pool in w_let.split()] * rep_pvt
        res = [[]]
        for pool in pools:
            res = [x + [y] for x in res for y in pool]
        for prod in res:
            print(''.join(tuple(prod)))
        return 'итого', len(res)
    else:
        raise TypeError('передан неверный тип данных')
