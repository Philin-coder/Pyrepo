import math


def format_func_again(d: float) -> [int, tuple]:
    """
    Иллюстрация работы с форматами
    :param d: число
    :return:результат подсчета, выводимый в формате
    >>> format_func_again(d=20.4)
    ('площадь окружности равна и длина', ' ', '326.8513', ' ', '  64')
    >>> format_func_again(d=20)
    ('площадь окружности равна и длина', ' ', '314.1593', ' ', '  63')

    """
    if isinstance(d, float) or isinstance(d, int):
        p = math.pi * d
        s = (math.pi * d * d) / 4
        return 'площадь окружности равна и длина', ' ', "%.4f" % s, ' ', "%4.f" % p
    else:
        raise TypeError('Введено не число ')
