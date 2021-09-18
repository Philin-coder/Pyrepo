def median_finder(n: int) -> [int, float]:
    """
    Поиск медианы списка
    :param n:  граница диапазона
    :return: медиана диапазона
    >>> median_finder(n=11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    6.5
    >>> median_finder(n=10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    5

    """
    if isinstance(n, int) and n != 0 and n > 0:
        ints = [i for i in range(1, n + 1)]
        print(ints)

        index = (len(ints) - 1) // 2
        if len(ints) % 2 == 0:
            return sorted(ints)[index]
        else:
            return (sorted(ints)[index] + sorted(ints)[index + 1]) / 2.0
    else:
        raise TypeError('Введите положительное, целое число не равное 0')


