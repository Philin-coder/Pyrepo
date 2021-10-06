import math


def f(x: float) -> float:
    """
    Вспомогтельная функция дя метода хорд
    :param x:входной параметр
    :return:резудьтат подсчета
    >>> f(x=12.0)
    -15.418879797456006
    >>> f1(x=11.0)
    -1.1978952727983705
    >>> chord_method(a=100.0, b=200.0)
    35.77152063957297

    """
    if isinstance(x, float) or isinstance(x, int):
        return 0.1 * math.pow(x, 2) - x * math.log(x)
    else:
        raise TypeError('Введено не число')


def f1(x: float) -> float:
    """
    Вспомогтельная функция дя метода хорд
    :param x:входной параметр
    :return:резудьтат подсчета
    """
    if isinstance(x, float) or isinstance(x, int):
        return 0.2 * x - math.log(x) - 1
    else:
        raise TypeError('Введено не число')


def chord_method(a: float, b: float) -> float:
    """
    Иллюстрация метода Хорд
    :param a: входной параметр
    :param b: входной параметр
    :return: резудьтат подсчета
    """
    if isinstance(a, float) or isinstance(b, float) or isinstance(a, int) or isinstance(b, int):
        try:
            x0 = (a + b) / 2
            xn = f(x0)
            xn1 = xn - f(xn) / f1(xn)
            while abs(xn1 - xn) > math.pow(10, -5):
                xn = xn1
                xn1 = xn - f(xn) / f1(xn)
            return xn1
        except ValueError:
            raise ValueError('Value not invalidate')
    else:
        raise TypeError('Введено не число')
