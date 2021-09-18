import re


def finder(str_input: str) -> int:
    """
    >>> finder(str_input='123wwwабв')
    ['а', 'б', 'в']
    3
    >>> finder(str_input='проба')
    ['п', 'р', 'о', 'б', 'а']
    5


    :param str_input: вводимый текст
    :return: количество русских букв в нем
    """
    if isinstance(str_input, str):
        regex_temp = re.compile("[а-яА-Я]+")
        russian = [i for i in filter(regex_temp.match, str_input)]
        print(russian)
        return len(russian)
    else:
        raise TypeError('Введите строку')
