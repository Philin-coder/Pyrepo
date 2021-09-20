def dict_gen_func() -> dict:
    """
    Пример создания словаря циклом
    :return: циклически созданных словарь
    >>> dict_gen_func()
    {'раз': 1, 'два': 2, 'три': 3}
    """
    if isinstance({k: i + 1 for i, k in enumerate(['раз', 'два', 'три'])}, dict):
        return {k: i + 1 for i, k in enumerate(['раз', 'два', 'три'])}
    else:
        raise TypeError('Получен не словарь')
