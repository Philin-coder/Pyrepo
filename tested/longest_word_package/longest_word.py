def long_word(text_str: str) -> [int, str]:
    """
    :param text_str: вводимая строка
    :return: словво(самое длинное ) и количество букв в в нем
    >>> long_word(text_str='Проба третья')
    {5: 'Проба', 6: 'третья'}
    (6, 'третья')
    >>> long_word(text_str='да нет')
    {2: 'да', 3: 'нет'}
    (3, 'нет')

    """
    if isinstance(text_str, str) and len(text_str) != 0:
        dx = dict([(len(x), x) for x in text_str.split()])
        print(dx)
        return max(dx), dx[max(dx)]
    else:
        raise ValueError('Введите строку')
