def changer(text_str: str, text_substr: str, repl_str: str) -> str:
    """
    Замена строки в подстроке га указанную
    :param text_str:текстовая строка
    :param text_substr: шаблон поиска
    :param repl_str:   строка для замегны
    :return:  результирующая строка
    >>> changer(text_str='Самая длинная река это Волга', text_substr='Волга',
    ...                   repl_str='Нил')
    'Самая длинная река это Нил'


    """
    if isinstance(text_str, str) and not any(i.isdigit() for i in text_str) and not any(
            i.isdigit() for i in text_substr) and isinstance(text_substr, str) and isinstance(repl_str,
                                                                                              str) and \
            not any(i.isdigit() for i in repl_str) and len(text_str) > 0 and len(text_substr) > 0 and len(repl_str) > 0:
        try:
            return text_str.replace(text_substr, repl_str)
        except (TypeError, ValueError):
            raise TypeError('Введите стору')
    else:
        raise ValueError('Проверьте, возможно, введена не строка ')
