def sum_more_ten(ints: list) -> int:
    """
    Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
    :param ints: исходный список.
    :return: сумма чисел больше 10
    >>> sum_more_ten(ints=[1, 3, 45, 6, 8, 11])
    56
    """
    if isinstance(ints, list) and all(isinstance(i, int) for i in ints):
        return sum([i for i in ints if i > 10])
    else:
        raise TypeError('Передан неверный  тип данных')
