def str_without_nums(mixed_str: str) -> str:
    """
    Из введенной пользователем строки удалить все числа, оставшееся записать в файл.
    :param mixed_str: исходная строка.
    :return: строка, не содержащая цифр.
    >>> str_without_nums(mixed_str='1s2t3o4p')
    'stop'

    """
    if isinstance(mixed_str, str) and any(i.isdigit() for i in mixed_str) and mixed_str != '':
        return ''.join(i for i in mixed_str if not i.isdigit())
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(file_name: str, f_ext: str, f_data: str) -> str:
    """
    Запись в файл.
    :param file_name: имя файла.
    :param f_ext: Расширение.
    :param f_data: То, что должно попасть в файл.
    :return:файл с нужными данными
    >>> write_to_file(file_name='test', f_ext='txt', f_data=str_without_nums(mixed_str='1s2t3o4p'))
    'file_created'

    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_data, file=fp, sep="\n")
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')
