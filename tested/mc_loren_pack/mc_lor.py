import math


def mck_loren(x: float, e: float, km: int) -> [tuple, float]:
    """
    >>> mck_loren(x=12.0, e=15.1, km=4)
    достигнутая точность= 1.0  сумма= 1  k= 0
    ('аналитически=', 81377.39571257407)

    Уравнение Мак лорена.
    :param x:Входной параметр.
    :param e: Входной параметр.
    :param km: Входной параметр.
    :return: Результат подсчета.
    """
    s = 1
    k = 0
    t = 1
    if isinstance(x, float) and isinstance(km, int) and isinstance(e, float):
        while math.fabs(t) > e:
            k += 1
            t = t * x * x / (2 * k * (2 * k - 1))
            s = s + t
            if k > km:
                print('При kmax=', km, ' ряд не сходится!')
                print('достигнутая точность=' + str(math.fabs(t)), 'сумма=', ' ', s)
                print('аналитически=', (math.exp(x) + math.exp(-x)) / 2)
        print('достигнутая точность=', math.fabs(t), ' сумма=', s, ' k=', k)
        return 'аналитически=', (math.exp(x) + math.exp(-x)) / 2
    else:
        raise TypeError('Передан неверный тип данных')
