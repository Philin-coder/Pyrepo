import numpy as np


def mas_summer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Пример суммирования массивов в numpy.
    :param a: массив а.
    :param b: массив а.
    :return: сумма массивов
    Пример вызова
    print(mas_summer(a=np.ndarray([1, 2, 3]), b=np.ndarray([1, 2, 3])))
    """
    if isinstance(a, np.ndarray) and isinstance(b, np.ndarray):
        return a + b
    else:
        raise TypeError('Передан неверный тип данных')
