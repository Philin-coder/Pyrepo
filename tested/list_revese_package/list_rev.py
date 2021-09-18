def list_reverse_gen(n: int) -> list:
    """
    :param n: вводимый аргумент -количество элементов списка(целое  положение число больше 0)
    :return: список от нуля, до введенного числа с шагом 1
    ввод 3
    вывод  0,1,2,3
    >>> list_reverse_gen(n=12)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> list_reverse_gen(n=2)
    [0, 1, 2]
    [2, 1, 0]
    >>> list_reverse_gen(n=4)
    [0, 1, 2, 3, 4]
    [4, 3, 2, 1, 0]


    """
    if isinstance(n, int):
        try:
            int_list = [i for i in range(n + 1)]
            print(int_list)
            int_list.reverse()
            return int_list

        except ValueError:
            raise ValueError('Должно быть введено целое, положительное число')
    else:
        raise ValueError('Должно быть введено целое, положительное число')
