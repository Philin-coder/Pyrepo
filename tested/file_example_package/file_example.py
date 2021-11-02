def generate_cont(data_str: [str, int]) -> [str, int]:
    """
    Функция генерации контента, который записывается в файл.
    :param data_str: вводимая строка.
    :return: то, что отправится в файл.
    >>> generate_cont(data_str='yes')
    'yes'
    """
    if data_str is not None and data_str != '' and isinstance(data_str, str):
        return data_str
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(filename: str, f_ext: str, f_data: str) -> str:
    """
    Запись информации в файл.
    :param filename:  имя файла.
    :param f_ext: расширение файла.
    :param f_data: Информациия, которую записываем в файл
    :return: код состояния(успешна, или нет запись).
    >>> write_to_file(filename='test', f_ext='txt', f_data=generate_cont(data_str='yes'))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            fp.write(f_data)
        stat_code = 'file_created'
        return stat_code
    else:
        raise TypeError('файл имеет неверное расширение')
