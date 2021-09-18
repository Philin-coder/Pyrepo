def t_ind_check(n: int) -> tuple:
    """
    Вызов по индексу из картежа
    :param n: диапазон значений
    :return: картеж с  первым , вторым  и минус третьего  элемнетами ( вызваны по индексу)
    >>> t_ind_check(n=5)
    (1, 2, 3, 4, 5)
    (1, 2, 3)
    >>> t_ind_check(n=14)
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    (1, 2, 12)


    """
    if isinstance(n, int) and n > 4:
        int_tuple = tuple(i for i in range(1, n + 1))
        print(int_tuple)
        ind_tuple = (int_tuple[0], int_tuple[1], int_tuple[-3])
        return ind_tuple
    else:
        raise TypeError('n вне допустимой области значенй')

