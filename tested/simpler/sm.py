import math


def is_prime(i: int) -> bool:
    """
    проверка  чисел в диапазоне на прстоиу
    :param i: и-тый элемент диапазона
    :return: True либо False при соответсвии, либо   несоответвии критерию (остаток, при дилении на 0)
    >>> is_prime(i=1)
    True
    >>> is_prime(i=21)
    False
    """
    if isinstance(i, int):
        return not any(map(lambda x: i % x == 0, range(2, min(i, int(math.sqrt(100000000))))))
    else:
        raise TypeError('Введено не число')


def list_gen(n: int) -> list:
    """
    формирование списка  простых чисел в диапазоне
    :param n: диапазон
    :return: список чисел
    >>> list_gen(n=100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    >>> list_gen(n=7)
    [2, 3, 5]
    >>> list_gen(n=1)
    []


    """
    if isinstance(n, int) and n > 0:
        return list(filter(is_prime, range(2, n)))
    else:
        raise TypeError('Введите положительное  число не равное 0')
