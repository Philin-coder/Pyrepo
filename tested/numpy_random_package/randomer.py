import numpy
import random


def numpy_random_func(n: int) -> list:
    """
    Работа с массивом numpy  при помощи random.
    :param n: диапазон
    :return: вектор
    Пример вызова: print(numpy_random_func(n=3))
    """
    if isinstance(n, int):
        return numpy.array([random.random() for _ in range(n)])
    else:
        raise TypeError('введите целое число')
