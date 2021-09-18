def list_sel_func() -> list:
    """
    Иллюстрация работы со списковыми включениями
    :return:   каждый четный элемент утраиваем(счет с 0), остальные удваиваем
    >>> list_sel_func()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [3, 4, 9, 8, 15, 12, 21, 16, 27, 20]

    """
    ints = [i for i in range(1, 11)]
    print(ints)
    return list((i * 3 if i % 2 else i * 2 for i in ints))
