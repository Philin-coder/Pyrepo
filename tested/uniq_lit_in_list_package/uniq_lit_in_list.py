def collect_unique(text_str: str) -> list:
    """
    Получение уникальных значений в строке, без set
    :param text_str: вводимая строка, должна быть разделена пробеламми
    :return: список уникальных литералов  строки
    >>> collect_unique(text_str='проба проба2 проба2')
    проба проба2 проба2
    ['проба', 'проба2']
    >>> collect_unique(text_str='проба1 проба2 проба3')
    проба1 проба2 проба3
    ['проба1', 'проба2', 'проба3']
    """
    if len(text_str) != 0 and isinstance(text_str,str):
        try:
            print(text_str)
            words = list()
            for i in text_str.split():
                if i not in words:
                    words.append(i)
            return words

        except ValueError:
            raise ValueError('введите строку')
    else:
        raise ValueError('введите строку')


