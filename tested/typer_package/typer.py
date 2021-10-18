def m_typ(a: str, x: str, b: str) -> [int, str]:
    """
    Демонстрация преобразования типов
    :param a:рабочач переменная
    :param x: рабочач переменная
    :param b: рабочач переменная
    :return: резулььтат арифметической операции
    >>> m_typ('1', '2', '4')
    -6
    """
    if isinstance(a, str) and isinstance(x, str) and isinstance(b, str):
        return int(x) * (int(a) - int(b))
    else:
        raise TypeError('Передан неверный тип данных')
