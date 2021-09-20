def cycle_dict_func(key_list: list) -> dict:
    """
    ПРИмер циклически созданого словаря
    :param key_list: список ключей словаря
    :return: словарь
    >>> cycle_dict_func(key_list=['раз', 'два', 'Три'])
    {'раз': 1, 'два': 2, 'Три': 3}

    """
    if isinstance(key_list, list):
        return dict(zip(key_list, range(1, 1 + len(key_list))))
    else:
        raise TypeError('Передане не списсок')
