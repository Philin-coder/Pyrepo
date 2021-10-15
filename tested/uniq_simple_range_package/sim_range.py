import math


def sim_list_func(n: int) -> bool:
    """
    уникальные простые числа в диапазоне до n
    :param n: числовой диапазон
    :return: проверка на простоту
    >>> sim_list_func(n=31)
    {0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    False

    >>> sim_list_func(n=3)
    {0, 1, 2}
    True
    >>> sim_list_func(n=-3)
    set()
    False

    """
    if isinstance(n, int):
        int_list = set()
        flag = False
        for i in range(n):
            flag = True
            for j in range(2, 1 + int(math.sqrt(i))):
                if not i % j:
                    flag = False
                    break
            if flag:
                int_list.add(i)
        print(int_list)
        return flag
    else:
        raise TypeError('введено не число')
