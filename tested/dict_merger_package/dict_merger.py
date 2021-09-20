def dict_mergers_func(names: list, surname: list, ags: list) -> dict:
    """
    ПРИмер слияния словарей
    :param names: словарь имен
    :param surname: словарь фамилий
    :param ags: словарь возоастов
    :return:  результирующий словарь, объединяющий все предыдущие
    >>> dict_mergers_func(names=[';;Люда', 'Тимафей;;', 'Петр;', ';;Яна', ';;Мефодий', ';Ксения;', 'Дамира'],
    ...                             surname=['Иванова', 'Джонс', 'Киселев', 'Солнцева', 'Петрова', 'Смирнова', 'Алексеева'],
    ...                             ags=[8, 34, 17, 2, 86, 32, 101])
    {'Люда Иванова': 8, 'Тимафей Джонс': 34, 'Петр Киселев': 17, 'Яна Солнцева': 2, 'Мефодий Петрова': 86, 'Ксения Смирнова': 32, 'Дамира Алексеева': 101}

    """
    if isinstance(names, list) and isinstance(surname, list) and isinstance(ags, list) and all(
            isinstance(i, str) for i in names) and all(isinstance(i, str) for i in surname) \
            and all(isinstance(i, int) for i in ags):
        for i in range(len(names)):
            names[i] = names[i].replace(';', '') + ' ' + surname[i]
        return dict(zip(names, ags))
    else:
        raise TypeError('Передан неверный тип данных')
