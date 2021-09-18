def inp_list(any_data: list) -> str:
    """

    :param any_data: данные, которые оттправляются в список
    :return:  тип возвращаемого значения(должен получаться list)
    >>> inp_list(any_data=[1, 2, 3])
    [1, 2, 3]
    'list'
    >>> inp_list(any_data=['3', 4, '5'])
    ['3', 4, '5']
    'list'
    >>> inp_list(any_data=[1, 2, 1.7])
    [1, 2, 1.7]
    'list'
    >>> inp_list(any_data=[1, 2, 3])
    [1, 2, 3]
    'list'
    """
    if type(any_data).__name__ == 'list':
        print(any_data)
        return type(any_data).__name__
    else:
        raise TypeError('Ввели  не лист')
