import roman


def roman_nums(text_str: str) -> int:
    """
    Перевод из римских цифр в арабские(библиотека roman)
    :param text_str: Римская цифра
    :return: арабская эквивалентная цифра
    >>> roman_nums(text_str='I')
    1
    >>> roman_nums(text_str='II')
    2
    >>> roman_nums(text_str='IV')
    4

    """
    if isinstance(text_str, str) and text_str.isupper():
        return roman.fromRoman(text_str)
    else:
        raise TypeError('Введите римскую цифру большими латинскими буквами')
