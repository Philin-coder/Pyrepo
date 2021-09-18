def sum_of_devs_func(x: int) -> int:
    """
    Сумма делителей числа
    :param x:  целое чмсло
    :return:  чумма его делителей(четнотсь )
    >>> sum_of_devs_func(x=12)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    78
    >>> sum_of_devs_func(x=15)
    []
    0
    >>> sum_of_devs_func(x=14)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    105
    >>> sum_of_devs_func(x=0)
    []
    0

    """

    if isinstance(x, int):
        ints = [i for i in range(1, x + 1) if x % 2 == 0]
        print(ints)
        return sum(ints)
    else:
        raise TypeError('Введите целое число')
