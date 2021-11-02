def generate_cont(data_lst: list) -> [list]:
    """
    запись списка в файл.
    :param data_lst:список.
    :return:результирующий список.
    >>> generate_cont(data_lst=[1, 2, 3])
    [1, 2, 3]
    """
    if data_lst is not None and isinstance(data_lst, list):
        return data_lst
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(filename: str, f_ext: str, f_data: list) -> [list, str]:
    """

    :param filename: имя файла.
    :param f_ext:  расширение.
    :param f_data: данные, которые будут записаны в файл
    :return: код состояния
    >>> write_to_file(filename='test', f_ext='txt', f_data=generate_cont(data_lst=[1, 2, 3]))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_data, file=fp, sep='\n')

        stat_code = 'file_created'
        return stat_code
    else:
        raise TypeError('файл имеет неверное расширение')
