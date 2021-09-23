import math


def solver_func(a: float, b: float, c: float) -> [str, tuple]:
    """
    Решение упавнения ax+bx+c=0
    :param a:коэффицента а
    :param b: коэффицента b
    :param c: коэффицента c
    :return:  результат уравнение
    >>> solver_func(a=12.0, b=12.0, c=12.0)
    ('квадратное уровнение корней не имеет', ' дискриминант равен -572.5358983848622')
    >>> solver_func(a=12, b=12, c=12)
    ('квадратное уровнение корней не имеет', ' дискриминант равен -572.5358983848622')
    >>> solver_func(a=5.0, b=400.0, c=1.0)
    ('-40.0', '-40.0', ' дискриминант равен 0.0')
    >>> solver_func(a=1.0, b=400.0, c=1.0)
    ('-198.0', ' -202.0', 'дискриминант равен 16.0')

    """
    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float) or isinstance(a, int) \
            or isinstance(b, int) or isinstance(c, int) and a != 0 and b != 0:
        try:
            f_dis = math.sqrt(b) - 4 * a * c
            if f_dis < 0:
                return f'квадратное уровнение корней не имеет', f' дискриминант равен {f_dis}'
            else:
                if f_dis == 0:
                    return f'{-b / (2 * a)}', f'{-b / (2 * a)}', f' дискриминант равен {f_dis}'
                else:
                    return f'{(-b + math.sqrt(f_dis)) / (2 * a)}', f' {(-b - math.sqrt(f_dis)) / (2 * a)}', \
                           f'дискриминант равен {f_dis}'
        except ZeroDivisionError:
            raise ZeroDivisionError('Нельзя делить  на  ноль')
    else:
        if not isinstance(a, int) or isinstance(b, int) or isinstance(c, int) or isinstance(a, float) or \
                isinstance(b, float) or isinstance(c, float):
            raise TypeError('Введите числа')
