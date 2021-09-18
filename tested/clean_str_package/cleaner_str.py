import re


def cleaner(text_str: str) -> str:
    """
    От трех букв оставляем 1
    :param text_str: ввод текста
    :return: вывод результирующей строки
    >>> cleaner(text_str='проооба')
    'проба'
    >>> cleaner(text_str='оса')
    'оса'

    """
    if isinstance(text_str, str):
        res = re.sub(r'([а-яa-z])\1(?=\1)', '', text_str)
        return res
    else:
        raise TypeError('Введите строку')


