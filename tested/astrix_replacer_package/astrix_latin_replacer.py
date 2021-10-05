def find_replacer_astrix_func(text_str: str) -> str:
    """
    Замена букв после звездочкии ена точки(в тексте на латинице), если звездочики нет, строка возвращается в исходном
    виде
    :param text_str: текстовая строка
    :return: результат замены
    'test'
    >>> find_replacer_astrix_func(text_str='kas*tle')
    4
    kas
    '...'
    >>> find_replacer_astrix_func(text_str='проб*а')
    5
    проб
    'проб'

    """
    if isinstance(text_str, str) and not any(i.isdigit() for i in text_str):
        for i in range(len(text_str)):
            if '*' not in text_str:
                return text_str
        else:
            print(int(text_str.find('*')) + 1)
            res = (text_str[:int(text_str.find('*')) + 1 - 1])
            print(text_str[:int(text_str.find('*')) + 1 - 1])
            for i in res:
                if (ord(i) >= 97) and (ord(i) <= 122) or ((ord(i) >= 41) and (ord(i) <= 90)):
                    res = res.replace(i, '.')

            return res
    else:
        raise TypeError('Введите  строку ')
