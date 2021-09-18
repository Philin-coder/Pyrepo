def list_func(n: int) -> int:
    """

    :param n: количество чисел
    :return: сумма чисел, кратных 5 и не делящихся на 9(n>99)
    >>> list_func(10)
    []
    0
    >>> list_func(100)
    [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    500
    >>> list_func(150)
    [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]
    1125
    >>> list_func(200)
    [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]
    2000
    >>> list_func(123)
    [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]
    720


    """

    if not isinstance(n, int):
        raise TypeError('Введено не число')
    else:
        int_list = [i for i in range(n) if i % 5 == 0 and i % 10 != 0 and n > 99]
        print(int_list)
        return sum(int_list)
