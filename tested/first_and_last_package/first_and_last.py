import re


def word_finder(text_str: str) -> list:
    """
    Поиск слов, начинающихся и заканчивающихся одной и той же буквой.
    :param text_str: строка, для поиска.
    :return: результирующий список.
    >>> word_finder(text_str='оно ото, которое (задание), само себя не сделает')
    [('оно', 'о'), ('ото', 'о')]
    """
    if isinstance(text_str, str) and text_str != '' and all(isinstance(i, str) for i in text_str):
        return re.findall(r'\b((\w)\w*\2)\b', text_str)
    else:
        raise TypeError('Передан неверный тип данных')
