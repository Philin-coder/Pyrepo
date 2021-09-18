def rus_w_lister(m_input_text: str) -> int:
    """
    Возввращает количество русских гласных букв во введенной строке

    :param m_input_text: строка, которая подается на вход
    :return: количество букв
    >>> rus_w_lister('Проверка раз')
    Проверка раз
    ['о', 'е', 'а', 'а']
    4
    >>> rus_w_lister('привет, мир')
    привет, мир
    ['и', 'е', 'и']
    3
    >>> rus_w_lister('привет,@@@@@@@@@@@@@@@@@@@@ мир')
    привет,@@@@@@@@@@@@@@@@@@@@ мир
    ['и', 'е', 'и']
    3

    """
    if not isinstance(m_input_text, str):
        raise TypeError('Необходимо вводить строки, не числа')

    elif isinstance(m_input_text, str):
        try:
            print(m_input_text)
            rus_w = ('а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я')
            print([i for i in m_input_text if i in rus_w])
            return len([i for i in m_input_text if i in rus_w])
        except TypeError:
            TypeError('Необходимо вводить строки, не числа')
