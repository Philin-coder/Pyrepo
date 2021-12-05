import random


def randomer(n: int) -> list:
    """
    Эмуляция лотереи 6 из 45.
    :param n: диапазон.
    :return: список чисел  без повторов
    """
    if isinstance(n, int) and n > 0:
        ints = [random.randint(5, n + 1) for _ in range(n)]
        random.shuffle(ints)
        return list(set(ints))
    else:
        raise TypeError('Передан неверный тип данных')
