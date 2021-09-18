def finder(text_str: str) -> bool:
    """
    2)Выяснить, имеется ли среди S1 … Sn пара соседствующих букв но или он.
    :param text_str: текст
    :return: true, либо false, в зависимости от того, есть ли ОН или НО(если есть, то True, иначе False)
    >>> finder(text_str='Проба  НО не победа')
    Проба  НО не победа
    True
    >>> finder(text_str='ОН оно но не онв')
    ОН оно но не онв
    True
    >>> finder(text_str='Проба  НО не победа')
    Проба  НО не победа
    True
    >>> finder(text_str='Проба   нет тут ничего не победа')
    Проба   нет тут ничего не победа
    False

    """
    if isinstance(text_str, str):
        print(text_str)
        allowed = ('НО', 'ОН')
        if any(i in text_str for i in allowed):
            return True
        else:
            return False
    else:
        raise TypeError('Вводите строку')
