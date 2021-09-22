def reverser_func(right_list: list) -> int:
    """
    Переворот списка, иллюстрация
    :param right_list: списоок числ
    :return: сумма числе в нем
    >>> reverser_func(right_list=[1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    15

    """
    if isinstance(right_list, list) and all(isinstance(i, int) for i in right_list):
        print(list(reversed(right_list)))
        return sum(right_list)
    else:
        raise TypeError('Передан неверный тип данных')
