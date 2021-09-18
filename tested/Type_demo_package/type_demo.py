def immut() -> tuple:
    """
    :return: возврат типа переданного значения
    >>> immut()
    "<class 'tuple'>"


    """
    test_tuple = (1, 1)
    if type(test_tuple).__name__ == 'tuple':
        return f'{type(test_tuple)}'
    else:
        raise TypeError('Подано значение неверного типа')
