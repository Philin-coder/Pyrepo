def min_and_index_func(ints: list) -> str:
    """
    Поиски минимума и его номера(илллюстрация format)
    :param ints: список чисел
    :return: минимум и его номер
    >>> min_and_index_func(ints=[4, 7, -3, 1, -7, 11, 6])
    'Минимальный 5-й элемент массива = -7'


    """
    if isinstance(ints, list):
        val, idx = min((val, idx) for (idx, val) in enumerate(ints))
        return 'Минимальный {}-й элемент массива = {}'.format(idx + 1, val)
    else:
        raise TypeError(f'Получен не список а, {type(ints).__name__}')



