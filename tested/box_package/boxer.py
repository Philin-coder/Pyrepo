import math


def box(s: float) -> float:
    """

    :param s:сторогы
    :return: общая площадь  3 сторон коробки
    >>> box(s=4)
    0.7698003589195009

    """
    if isinstance(s, int):
        h = 0.5 * math.sqrt(s / 3.0)
        return math.sqrt(s / 3.0) * math.sqrt(s / 3.0) * h
    else:
        raise TypeError('должно быть введено целое число')
