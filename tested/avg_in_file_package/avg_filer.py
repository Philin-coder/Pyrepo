def int_list_gen(n: int) -> list:
    """
    :param n: диапазон
    :return: результирующий список\
    >>> int_list_gen(n=10)
    [1.0, 1.148698354997035, 1.3903891703159095, 1.7411011265922482, 2.23606797749979, 2.9301560515835217, 3.9045287771
    22722, 5.278031643091578, 7.224674055842077, 10.000000000000002]
    """
    if isinstance(n, int):
        int_list = [i for i in range(-10, n + 1) if i > 0]
        res_list = [(i ** i) ** (1 / len(int_list)) for i in int_list if i > 0]
        return res_list
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(file_name: str, f_ext: str, data_lst: list) -> str:
    """
    Запись данных в файл.
    :param file_name: имя файла.
    :param f_ext: расширение файла.
    :param data_lst: данные, которое уйдут в файл.
    :return:
    >>> write_to_file(file_name='test', f_ext='txt', data_lst=int_list_gen(n=10))
    'file_created'

    """
    if isinstance(f_ext, str) and isinstance(data_lst, list) and all(
            isinstance(i, float) for i in data_lst) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(data_lst, file=fp, sep="\n")
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверное расширение, либо - передан неверный тип данных')
