def max_and_ind_func(n: int, cycle_step: int) -> str:
    """
    :param n: конец диапазона
    :param cycle_step: шаг по диапазону
    :return:  максимум диапазона и его номер
    >>> max_and_ind_func(n=12, cycle_step=2)
    [1, 3, 5, 7, 9, 11]
    ' макссимум =11, его номер =5'
    >>> max_and_ind_func(n=12, cycle_step=1)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ' макссимум =12, его номер =11'

    """
    if isinstance(n, int) and isinstance(cycle_step, int) and cycle_step > 0:
        ints = [i for i in range(1, n + 1, cycle_step)]
        print(ints)
        return f' макссимум ={max(ints)}, его номер ={ints.index(max(ints))}'
    else:
        raise ValueError('Введите 2 целых числа граница диапазона и шаг')


