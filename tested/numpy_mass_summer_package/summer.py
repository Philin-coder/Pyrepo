import numpy as np


def mas_summer(a: np.matrix, b: np.matrix) -> np.matrix:
    """
    Пример суммирования массивов в numpy.
    :param a: массив а.
    :param b: массив а.
    :return: сумма массивов
    Пример вызова
    >>> mas_summer(a=np.matrix([[11, 22], [33, 44]]), b=np.matrix([[55, 66], [77, 88]]))
    matrix([[ 66,  88],
            [110, 132]])

    """
    if isinstance(a, np.matrix) and isinstance(b, np.matrix):
        return np.add(a, b)
    else:
        raise TypeError('Передан неверный  тип данных')


if __name__ == '__main__':
    mas_summer(a=np.matrix([[11, 22], [33, 44]]), b=np.matrix([[55, 66], [77, 88]]))
    mas_summer(a=np.ndarray([[11, 22], [33, 44]]), b=np.ndarray([[55, 66], [77, 88]]))
