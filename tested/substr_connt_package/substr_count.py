def inp_counter_func(text_string: str, text_substr: str) -> int:
    """
    Подсчет вхождений подстроки в строку
    :param text_string: входная строка
    :param text_substr: подстрока
    :return: количество вхождений подстроки в строку
    >>> inp_counter_func(text_string='проба проба проба', text_substr='проба' )
    3

    """
    if isinstance(text_string, str) and isinstance(text_substr, str) and len(text_substr) > 0 and len(text_string) > 0:
        return text_string.count(text_substr)
    else:
        raise TypeError('Введите непустую строку')
