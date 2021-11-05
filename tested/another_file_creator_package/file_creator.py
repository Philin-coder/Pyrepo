def cont_gen(data: str) -> str:
    """
    Генерация контента для записи в файл.
    :param data: исходная строка.
    :return: Данные, готовые для записи в файл
    >>> cont_gen(data='test')
    'test'
    """
    if isinstance(data, str) and data != '' and data is not None:
        return data
    else:
        raise TypeError('Передан неверный тип данных')


def file_gen(my_f_name: str, f_ext: str, f_data: str) -> str:
    """
    Запись в файл.
    :param my_f_name:Имя файла.
    :param f_ext: Расширение.
    :param f_data: Данные, которые будут записаны в файл.
    :return: Код состояния(успешна ли запись).
    >>> file_gen(my_f_name='test', f_ext='txt', f_data=cont_gen(data='ПРОба2'))
    'file_created'
    """
    if isinstance(f_data, str) and f_ext == 'txt':
        fp = open(my_f_name + '.' + f_ext, 'w', encoding='utf-8')
        print(f_data, file=fp, sep='\n')
        fp.close()
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')
