def range_filter(n: int) -> list:
    """
    :param n: ввод количествоо элементов списка

    :return: список чисел подходящих условию(в данном случае : элемент списка >5)
    >>> range_filter(n=12)
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    >>> range_filter(n=5)
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    >>> range_filter(n=22)
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    """
    if not isinstance(n, int):
        raise TypeError('должно быть введено целое, положительное число не равное 0 ')
    else:
        int_list = range(1, 20)
        print(*int_list)
        return [i for i in int_list if i > 5]
