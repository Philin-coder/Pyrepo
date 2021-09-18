import math


def simple_expr(x, y, z):
    """
    :param x: параметр
    :param y: параметр
    :param z: параметр
    :return: резульат подсчета
    >>> simple_expr(x=0.1722, y=6.33, z=172.025)
    0.8536129750647968

    """
    y = 5 * math.atan(x) - (1 / 4) * math.acos(x) * ((x + 3) - math.fabs(x - y) + (x * x)) / (
            math.fabs(x - y) * z + (x * x))
    return y
