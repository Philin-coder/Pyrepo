def dig_pal_func(data: int) -> str:
    """
    Числовой палиндром
    :param data:  целое числ число
    :return: результа проверки на полиндромность
    >>> dig_pal_func(data=1213)
    'Число  не являетмся палиндроом'
    >>> dig_pal_func(data=123)
    'Число являетмся палиндроом'

    """
    if isinstance(data, int):
        data = str(data)
        for i in range(len(data) // 2):
            if data[i] != data[-i - i]:
                return 'Число  не являетмся палиндроом'

        else:
            return 'Число являетмся палиндроом'
    else:
        raise TypeError('Введите число')
