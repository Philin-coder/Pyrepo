def fib_fnd_func(n: int, x: int) -> [tuple, str]:
    """
    Поиски итого чмсла Фибаначчи в списке
    :param n: диапазон
    :param x: искомое число
    :return: если число есть в списке, возвращает число, иначе, возвращает соответствующее сообщение
    >>> fib_fnd_func(n=12, x=1)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    'число 1 содержится в списке'
    >>> fib_fnd_func(n=12, x=99)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    'числа  нет в диапазоне'

    """
    if isinstance(x, int) and isinstance(n, int):
        ints = [0, 1]
        for i in range(2, n + 1):
            ints.append(ints[i - 1] + ints[i - 2])
        print(ints)
        if x in ints:
            return f'число {ints[x]} содержится в списке'
        else:
            return 'числа  нет в диапазоне'
    else:
        raise TypeError('Введите числа')
