def before_colons_del(text_str: str) -> str:
    """

    :param text_str: текстовая строка, из которой удаляются символы после двое точия
    :return: результат
    >>> before_colons_del(text_str='проба: первая')
    проба: первая
    'проба'
    >>> before_colons_del(text_str='проба вторая')
    проба вторая
    'проба втора'
    >>> before_colons_del(text_str='colons: двоеточие')
    colons: двоеточие
    'colons'




    """
    if isinstance(text_str, str):
        print(text_str)
        return text_str[:text_str.find(':')]
    else:
        raise TypeError('введите строку')


