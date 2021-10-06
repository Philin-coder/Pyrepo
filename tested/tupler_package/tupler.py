def tuple_conv_func(text_srt: str) -> [tuple]:
    """
    Конвертация строки в кортеж
    :param text_srt: текствовая строка
    :return:  результирующий кортеж
    >>> tuple_conv_func(text_srt='hello')
    hello
    <class 'str'>
    <class 'tuple'>


    """
    if isinstance(text_srt, str):
        print(text_srt)
        print(type(text_srt))
        mt = tuple(text_srt)
        return type(mt)
    else:
        raise TypeError('Введите строку')
