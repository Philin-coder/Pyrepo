def phi(n: int) -> [int, float]:
    """
    Функция Эйлера
    :param n: количество элементов в плследовательности
    :return:  количество взаимно простых чисел  на интервале
    >>> phi(n=12)
    2.0
    >>> phi(n=10)
    4.0

    """
    if isinstance(n, int):
        result = n
        i = 2
        while i ** 2 < n:
            while n % i == 0:
                n /= i
                result -= result / i
            i += 1
        if n > 1:
            result -= result / n
        return result
    else:
        raise TypeError('Введите целое число')
