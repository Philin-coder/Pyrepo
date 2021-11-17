g_name = 'Bob'


def user_name(text_string: str) -> [str, tuple]:
    """
    Иллюстрация работы  с глобальными переемными.
    :param text_string: заменяемая строка.
    :return: то, что вернет функция, учитывая глобальнyю переменная.
    >>> user_name(text_string='jack')
    ('hello,jack', 'But global name is,Bob')
    """
    if isinstance(text_string, str):
        return 'hello' + ',' + text_string, 'But global name is' + ',' + g_name
    else:
        raise TypeError('Передан неверный тип данных')


def global_name() -> [str, tuple]:
    """
    Вывод глобальной переменной.
    :return: результирующая строка.
    >>> global_name()
    'my global name=Bob'
    """
    if isinstance(g_name, str):
        return 'my global name=' + g_name
    else:
        raise TypeError('Передан неверный тип данных')
