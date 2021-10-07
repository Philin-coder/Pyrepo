def factorial_func(n: int) -> int:
    """
    Отыскание факториала
    :param n: чмсло
    :return: факториал числа
    >>> factorial_func(n=3)
    6
    """
    if isinstance(n, int):
        if n == 0:
            return 1
        return factorial_func(n - 1) * n
    else:
        raise TypeError('Введите целое число')
