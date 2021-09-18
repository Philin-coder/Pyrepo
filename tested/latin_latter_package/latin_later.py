import string


def stringer() -> str:
    """
    Получить все латинские буквы
    :return:  строка латинских букув в малом и большом регистре
    >>> stringer()
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    """
    return f'{string.ascii_letters}'
