from collections import Counter


def find_common_func(mixed_values: list) -> [int, str]:
    """
    Частотный анализ списка
    :param mixed_values: список значений
    :return: самое часто встречаемое значение
    [1, 2, 4, 5, 6, 7, 7, 7, 7, 7, 8]
    7
    >>> find_common_func(mixed_values=['a', 'b', 'c', 'd', 'd', 'd'])
    ['a', 'b', 'c', 'd', 'd', 'd']
    'd'

    """
    if isinstance(mixed_values, list):
        print(mixed_values)
        return Counter(mixed_values).most_common()[0][0]
    else:
        raise TypeError('передан не список')
