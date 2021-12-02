import re


def num_finder(text_str: str) -> list:
    """
    Извлечь цифры из строки.
    in abc83 cde7 1 b 24
    out 83 7 1  24
    :param text_str:текстовая строка.
    :return:список чисел.
    >>> num_finder(text_str='abc83 cde7 1 b 24')
    [83, 7, 1, 24]
    """
    if isinstance(text_str, str) and text_str is not None and any(i.isdigit() for i in text_str) \
            and (i.isalpha() for i in text_str):
        return list(map(int, re.findall(r'\d+', text_str)))
    else:
        raise TypeError('Передан неверный тип данных, либо - пустая строка')
