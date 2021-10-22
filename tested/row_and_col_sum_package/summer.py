def row_plus_col(n: int, m: int) -> list:
    """
    Сумма каждой строки с столбца
    :param n:длинна  первого  сприска чисел
    :param m:длинна  второго сприска чисел
    :return: сумма каждой строки и столбца обоих списков
    >>> row_plus_col(n=3, m=5)
    [4, 6]

    """

    a_list = [i for i in range(1, n)]
    b_list = [i for i in range(3, m)]
    if all(isinstance(i, int) for i in a_list) and all(isinstance(i, int) for i in b_list) and isinstance(n, int) \
            and isinstance(m, int):
        try:
            return list(map(sum, zip(a_list, b_list)))

        except(TypeError, ValueError):
            raise TypeError('TypeError: str object cannot be interpreted as an integer')
