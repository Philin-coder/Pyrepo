def apply_example(x, y, z, a=None, b=None) -> tuple:
    """
    Пример функции apply
    :param x: элемент картежа
    :param y: элемент картежа
    :param z: элемент картежа
    :param a: элемент картежа
    :param b: элемент картежа
    :return: итоговый картеж
    >>> apply_example(*[1, 2, 3], **{'a': 4, 'b': 5})
    (1, 2, 3, 4, 5)
    """
    return x, y, z, a, b
