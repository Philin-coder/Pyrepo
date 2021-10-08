def sum_of_devs(x: int) -> int:
    """
    :param x:  целое положительное число. Определить сумму его делителей.
    :return: сумма его делителей
    >>> sum_of_devs(x=128)
    [1, 2, 4, 8, 16, 32, 64, 128]
    255
    >>> sum_of_devs(x=12)
    [1, 2, 3, 4, 6, 12]
    28

    """
    if not isinstance(x, int):
        raise TypeError('Введите целое число')
    else:
        devs = [i for i in range(1, x + 1 // 2 + 1) if x % i == 0]
        print(devs)
        return sum(devs)
