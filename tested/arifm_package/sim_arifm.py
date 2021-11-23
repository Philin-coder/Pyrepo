import math


def perv(a: int) -> float:
    """
    Отыскание первообразой.
    :param a: число
    :return: первообразная от него
    >>> perv(a=12)
     8.71673
    >>> perv(a=7)
    1.76643
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
    'точное значение интеграла 8.44406'
    """
    if isinstance(x, float) and isinstance(y, float):
        res = x - y
        return f'точное значение интеграла {res:.5f}'
    else:
        raise TypeError('Передан неверный тип данных')
