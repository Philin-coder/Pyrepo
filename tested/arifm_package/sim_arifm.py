import math


def perv(a: int) -> float:
    """
    Отыскание первообразой.
    :param a: число
    :return: первообразная от него
    >>> perv(a=12)
    8.71673508601987
    >>> perv(a=7)
    1.766437127533977
    """
    if isinstance(a, int):
        return 0.5 * a - 0.25 * a * math.sin(2 * a)
    else:
        raise TypeError('передан неверный тип данных')


def suber(x: float, y: float) -> [float, str]:
    """
    вычитание первообразоых.
    :param x: первое значение.
    :param y: второе.
    :return: результат.
    >>> suber(x=perv(a=12), y=perv(a=1))
    'точное значение интеграла 8.44405944272629'
    """
    if isinstance(x, float) and isinstance(y, float):
        return f'точное значение интеграла {x - y}'
    else:
        raise TypeError('Передан неверный тип данных')
