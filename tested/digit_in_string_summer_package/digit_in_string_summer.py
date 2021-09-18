def digit_summer_func(text_str) -> int:
    """
    сумма цифр в строке
    :param text_str:  вводтимая строка(содержащая цифры)
    :return:  сумма цифр в ней
    >>> digit_summer_func(text_str='лес 123 поле 356')
    [1, 2, 3, 3, 5, 6]
    20
    >>> digit_summer_func(text_str='лес, дол,   поле ')
    []
    0
    >>> digit_summer_func(text_str='123')
    [1, 2, 3]
    6

    """
    if isinstance(text_str, str) and len(text_str) > 0:
        symbols = (i for i in text_str if i.isdigit())
        ints = list(map(int, symbols))
        print(ints)
        return sum(ints)
    else:
        raise TypeError('Введите непустую строку, содержащую цифры')
