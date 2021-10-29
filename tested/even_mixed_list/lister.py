import re


def even_finder(mixed_vals: list) -> list:
    """
    ***1*** Дан произвольный список, содержащий и строки и числа.
    Выведите все четные элементы построчно (нужно вводить элементы списка через консоль).
    :param mixed_vals: исходный список.
    :return: результирующий список.
    >>> even_finder(mixed_vals=[1, 2, 3, 4, 6, 7, 9, 'a'])
    [2, 4, 6]

    """
    if isinstance(mixed_vals, list) and len(mixed_vals) > 0:
        fnd = str(mixed_vals).removesuffix(']').removeprefix('[')
        if any(isinstance(i, int) for i in mixed_vals):
            num_lst = list(map(int, re.findall(r'\d+', fnd)))
            return [i for i in num_lst if i % 2 == 0]
    else:
        raise TypeError('передан не список, или-список пуст ')
