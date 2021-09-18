def func(a: int, b: int) -> int:
    """
    Пример прстой функции, должен анрнуть сумму 2 чисел
    :param a: первое словгаемое
    :param b: второе
    :return: результат

    >>> func(2,2)
    4
    >>> func(3,4)
    7
    >>> func(1,7)
    8
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('проверьте входные данные')
    return a + b
