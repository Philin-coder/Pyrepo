def is_prime_func(n: int) -> [list, set]:
    """
    Простые числа на интервале до n
    :param n:  конец диапазона
    :return:  список простых чисел интервале
    >>> is_prime_func(n=12)
    [1, 2, 3, 5, 7, 11]
    >>> is_prime_func(n=2)
    [1, 2]
    """
    int_list = []
    if isinstance(n, int) and n > 0 and n != 0:
        for n in range(1, n + 1):
            if all(n % i != 0 for i in range(2, n)):
                int_list.append(n)

        return int_list
    else:
        raise TypeError('Введите целое полложительное число не равное 0')
