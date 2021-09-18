def int_list_gen(n: int) -> list:
    """
    :param n: целое положительное число не равное 0(количество элементов списка)
    :return: список, выведенный реверсом
    Ввод 12
    Вывод :
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> int_list_gen(4)
    [0, 1, 2, 3, 4]
    [4, 3, 2, 1, 0]
    >>> int_list_gen(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> int_list_gen(0)
    [0]
    [0]

    """
    if isinstance(n, int):
        try:
            int_list = [i for i in range(n + 1)]
            print(int_list)
            return int_list[::-1]

        except(ValueError, TypeError):
            raise ValueError('Должно быть введено целое, положительное число')
    else:
        raise TypeError('Должно быть введено целое, положительное число')
