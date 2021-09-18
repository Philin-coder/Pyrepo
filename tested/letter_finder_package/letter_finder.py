import doctest


def finder(text_str: str) -> bool:
    """
     Даны символы в строке. Выяснить, имеются ли в все буквы,входящие в слово «мир»
    :param text_str:  строка подаваемая на вход
    :return:  True или False в зависимости от результата(True, если есть хоть ожна буква, иначе False)
    >>> finder('мир')
    мир
    True
    >>> finder('рим')
    рим
    True
    >>> finder('кот')
    кот
    False
    >>> finder('тип')
    тип
    False

    """
    if not isinstance(text_str, str):
        raise TypeError('Необходимо вводить не пустую строку')
    elif len(text_str) > 0:
        try:
            print(text_str)
            let_to_find = ('м', 'и', 'р')
            if all(i in text_str for i in let_to_find):
                return True
            else:
                return False

        except ValueError:
            raise ValueError('введите  строку ')
    else:
        raise ValueError('Cтрока пуста')



