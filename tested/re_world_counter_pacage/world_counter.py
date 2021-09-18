import re


def wordcount(text_str: str) -> int:
    """
    :param text_str: текстовая строка, разделеная пробелами
    :return:  количество слов в строке
    >>> wordcount(text_str='проба первая')
    ['проба', 'первая']
    2
    >>> wordcount(text_str='проба вторая 1112')
    ['проба', 'вторая', '1112']
    3

    """
    if isinstance(text_str, str):
        result = re.findall(r'\w+', text_str)
        print(result)

        return len(result)
    else:
        raise TypeError('Введите строку, через пробел')


