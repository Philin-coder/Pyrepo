def inp_list(ints: list) -> list:
    """
    ввод  пользоваьелем списка целых чисел
    :param ints:  список, который вводит пользователь
    :return: список, получаемый пользователем
    >>> inp_list([1, 2, 3])
    [1, 2, 3]
    >>> inp_list([4, 6, 1])
    [4, 6, 1]
    >>> inp_list([3,2,1])
    [3, 2, 1]
    >>> inp_list([])
    >>>

    """
    for i in ints:
        if isinstance(i, int):
            return ints
        else:
            raise TypeError('В списке должны быть целые числа, он не должен быть пуст')
