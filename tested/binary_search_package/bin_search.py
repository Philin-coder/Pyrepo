def list_gen(n: int, value: int) -> [str, tuple]:
    """
    Биенарный поиск по списку
    :param n: диапазон
    :param value: искомое число
    :return: положенеи числа в списке
    Создание списка,
    его сортировка по возрастанию
    и вывод на экран
    >>> list_gen(n=100, value=21)
    [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
    ('ID =', 2)
    >>> list_gen(n=100, value=80)
    [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
    'No value'
    """
    if isinstance(n, int) and isinstance(value, int):
        ints = list(reversed(range(1, n + 1, 10)))
        ints.sort()
        print(ints)
        mid = len(ints) // 2
        low = 0
        high = len(ints) - 1
        while ints[mid] != value and low <= high:
            if value > ints[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            return 'No value'
        else:
            return 'ID =', mid
    else:
        raise TypeError('Введите числа')
