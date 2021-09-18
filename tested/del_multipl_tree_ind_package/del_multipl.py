def del_index(input_text_string: str) -> str:
    """
    Удаленеи из строки символов,индекс которых кратен 3
    :param input_text_string: текстовая строка
    :return: результирующая строка в которй удалены символы, кратные 3(по индексу,счет с 0 )
    >>> del_index(input_text_string='горе')
    'ор'
    >>> del_index(input_text_string='горемыка')
    'ормыа'
    >>> del_index(input_text_string='hold Fast')
    'ol Fst'

    """
    if isinstance(input_text_string, str) and not any(i.isdigit() for i in input_text_string) and len(
            input_text_string) > 0:
        return ''.join(letter for index, letter in enumerate(input_text_string) if index % 3 != 0)
    else:
        raise TypeError('Введена не строка')


