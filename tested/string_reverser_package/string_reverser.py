def string_reverser_func(text_str: str) -> [str, list]:
    """
    Переворот вводимой строки
    вводится строка
    :return:  выходная строка, в которой слова стоят наоборот
    >>> string_reverser_func(text_str='проба первая')
    'первая проба'

    """
    if isinstance(text_str, str) and len(text_str) > 0:
        sep = ' '
        res = sep.join(text_str.split()[::-1])
        return res
    else:
        raise TypeError('Введите непустую строку')
