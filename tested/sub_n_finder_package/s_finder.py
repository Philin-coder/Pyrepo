import re


def finder(sym: str, str_text: str) -> tuple:
    """
    Поиск и подсчет любых символов в строке
    :param sym: вводимый символов
    :param str_text: строка
    :return: строка и  количество искомых  символов в ней
    >>> finder(sym='о', str_text='дорога')
    ('дорога', 2)
    >>> finder(sym='о', str_text='Вологда')
    ('Вологда', 2)
    >>> finder(sym='а', str_text='Мама')
    ('Мама', 2)
    >>> finder(sym='x', str_text='Trixter')
    ('Trixter', 1)

    """
    if isinstance(sym, str) and isinstance(str_text, str):
        return re.subn(sym, sym, str_text)
    else:
        raise TypeError('Введите символ(не число) и строку для поиска')
