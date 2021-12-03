import math


def count_func(x: [float, int]) -> float:
    """
    Отыскание значения функции.
    :param x: переменная типа float,либо int.
    :return:Результат подсчета.
    >>> count_func(x=8)
    0.22
    >>> count_func(x=80.0)
    -1.5
    """
    if isinstance(x, float) or isinstance(x, int) and x is not None:
        try:
            return float(f'{2 * math.sqrt(x) * ((math.cos(x ** 2)) / 10):.2f}')
        except ValueError:
            raise ValueError('под корнем отрицательное число')

    else:
        raise TypeError('Передан неверный тип данных')
