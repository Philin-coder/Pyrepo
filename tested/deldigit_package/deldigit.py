def del_digit_func(text_with_digit_str: str) -> str:
    """

    :param text_with_digit_str: строка с с числами
    :return:  текстовая строка без цифр
    Входные данные: 123абы
    Выходные данные абы
    >>> del_digit_func('123s')
    's'
    >>> del_digit_func('123')
    ''
    >>> del_digit_func('апрооьепробгоьлдюолджю.123')
    'апрооьепробгоьлдюолджю.'
    >>> del_digit_func('sd/d////////.123')
    'sd/d////////.'



    """
    if len(text_with_digit_str) == 0:
        raise ValueError('проверьте входные данные(строка не должна быть пустой')

    return ''.join((i for i in text_with_digit_str if not i.isdigit()))
