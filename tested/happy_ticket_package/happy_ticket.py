def happy_ticket_func(text_str: str) -> str:
    """
     Счастливым считается билет, в шестизначном номере которого сумма первых
     трёх цифр совпадает с суммой трёх последних.
    :param text_str:номер билета
    :return:стчастливость билета
    >>> happy_ticket_func(text_str='123321')
    'Счастливый'
    >>> happy_ticket_func(text_str='114111')
    'Обычный'

    """
    if isinstance(text_str, str) and len(text_str) > 0:
        if sum([int(char) for char in text_str[:3]]) == sum([int(char) for char in text_str[-3:]]):
            return 'Счастливый'
        else:
            return 'Обычный'
    else:
        raise TypeError('введите строку(номер билета 6 знаков)')
