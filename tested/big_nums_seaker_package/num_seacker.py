import re


def string_big_digit_finder(text_str: str) -> list:
    """
    Поиск больших чисел в строке
    :param text_str: текстовая строка
    :return:  список найденных в ней чисел
    >>> string_big_digit_finder(text_str='1.152000000000D+05-1.303851604462D-07-5.331575505977D-01-3.986060619354D+07')
    1.152000000000D+05-1.303851604462D-07-5.331575505977D-01-3.986060619354D+07
    ['1.152000000000', '+05', '-1.303851604462', '-07', '-5.331575505977', '-01', '-3.986060619354', '+07']
    >>> string_big_digit_finder(text_str='Мир 1')
    Мир 1
    ['1']

    """
    if isinstance(text_str, str) and any(i.isdigit() for i in text_str) and len(text_str) > 0:
        print(text_str)
        return re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', text_str)
    else:
        raise TypeError('Передана строка, не содержащая цифр в нужном формате, либо - пустая')
