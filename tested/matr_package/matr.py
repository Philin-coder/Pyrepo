def matrix_gen(a: int, b: int) -> None:
    """
    Матрица из 1 и 0
    :param a: столбцов в матрице
    :param b: строк в матрице
    :return: маттрица из 1 и 0
    >>> matrix_gen(a=2, b=2)
    [0, 1]
    [0, 1]
    """
    if isinstance(a, int) and isinstance(b, int):
        m = [i if i == 0 else 1 for i in range(a)]

        n = [[j for j in m] for i in range(b + 1)]
        for i in range(b):
            print(n[i], sep="\n")
            return n[i]
    else:
        raise TypeError('Введены не числа')


