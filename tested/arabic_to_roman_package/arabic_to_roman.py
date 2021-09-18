def arabic_to_roman_func(n: int) -> str:
    """
    Перевод арабских цифр в римские
    :param n: арабская цира
    :return: римская цифпа, которая соответствует арабской
    >>> arabic_to_roman_func(n=12)
    'XII'
    >>> arabic_to_roman_func(n=8)
    'VIII'
    >>> arabic_to_roman_func(n=5)
    'V'
    >>> arabic_to_roman_func(n=128)
    'CXXVIII'

    """
    if isinstance(n, int) and n > 0 and n != 0:
        result = ''
        for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                                 'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
            result += n // arabic * roman
            n %= arabic

        return result
    else:
        raise TypeError('Должно быть введено целое  положительное число, не равное 0')


