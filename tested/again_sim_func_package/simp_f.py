def func(a: [int, str], b: [int, str]) -> [int, str]:
    """
    Иллюстрация передачи даннных по функциям
    :param a: рабочая переменная
    :param b:вторая рабочая переменная
    :return: сложение данных переменых
    >>> func2(func(a=2, b=5))
    7
    >>> func2(func(a='hello', b='world'))
    'helloworld'
    """

    if isinstance(a, int) and isinstance(b, int) or isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError('Передан неверный тип данных')


def func2(arg: [int, str]) -> [int, str]:
    return arg
