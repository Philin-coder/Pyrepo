import random


def mass_gen(n: int) -> [tuple, list[int]]:
    """
    Сопоставить минимум массива с каждым элементом.
    :param n: число элементов.
    :return: кортеж элементов и минимум.
    Образец вызова
    mass_gen(n=12)
    [1, (1, 3), (1, 4), (1, 6), (1, 3), (1, 3), (1, 10), (1, 4), (1, 4), (1, 4), (1, 10), (1, 8)]
    """
    if isinstance(n, int):
        mlist = [random.randint(1, 10) for _ in range(n)]
        minim = min(mlist)
        for i in range(1, len(mlist)):
            mlist[i] = minim, mlist[i]
        return mlist
    else:
        raise TypeError('передан неверный тип данных')
