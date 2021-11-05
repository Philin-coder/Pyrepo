def cont_gen(text_str: str) -> list:
    """
    Удаление цифр из строки.
    :param text_str: текстовая стока, содержащая цифры.
    :return: цифр из этой строки.
    >>> cont_gen(text_str='1s2t3o4p')
    [1, 2, 3, 4]
    """
    if isinstance(text_str, str) and any(i.isdigit() for i in text_str):
        nums = list(map(int, ''.join(i for i in text_str if i.isdigit())))
        return nums
    else:
        raise TypeError('Передан  неверный тип данных')


def write_file(file_name: str, f_ext: str, ls_data: list) -> str:
    """
    Запись в Файл.
    :param file_name:имЯ ФайлА.
    :param f_ext: Расширение.
    :param ls_data: данные, которые должны быть записаны в файл
    :return: Индикатор состояния(успешна ли запись).
    >>> write_file(file_name='test', f_ext='txt', ls_data=cont_gen(text_str='1s2t3o4p'))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(ls_data, file=fp, sep="\n")
            stat_code = 'file_created'
            return stat_code

    else:
        raise ValueError('Файл имеет неверное расширение')
