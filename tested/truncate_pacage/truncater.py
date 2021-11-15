import os


def cont_gen(c_str: str) -> str:
    """
    Генерация контента для записи в файл.
    :param c_str: строка, которая будет записана в файл.
    :return: Данные, записываемые в файл.
    Образец вызова
    cont_gen(c_str='to_be_truncated_string')
    'to_be_truncated_string'
    """
    if isinstance(c_str, str) and c_str != '':
        return c_str
    else:
        raise TypeError('Передан неправильный тип данных, либо - пустая строка')


def write_to_file(my_filename: str, f_ext: str, fdata: str) -> str:
    """
    Запись данных в файл
    :param my_filename: Имя файла.
    :param f_ext: Расширение.
    :param fdata: Записываемые данные.
    :return: код состояния(успешна ли  запись )
    Образец вызова
    write_to_file(my_filename='tr_test', f_ext='txt', fdata=cont_gen(c_str='to_be_truncated_string'))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(my_filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(fdata, file=fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')


def reader(my_filename: str, f_ext: str) -> list:
    """
    Чтение файла.
    :param my_filename: имя файла.
    :param f_ext: расширение.
    :return:Данные,прочитанные из файла.
    Образец вызова
    reader(my_filename='tr_test', f_ext='txt')
    ['to_be_truncated_string\n'
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = fp.readlines()
        return data
    else:
        raise FileNotFoundError('Такого файла нет')


def trunc(my_filename: str, f_ext: str) -> str:
    """
    Очистка файла.
    :param my_filename: имя файла.
    :param f_ext: расширение.
    :return: код состояния(очищен ли файл).
    Образец вызова
    trunc(my_filename='tr_test', f_ext='txt')
    'file_truncated'
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        fp = open(my_filename + '.' + f_ext, 'w', encoding='utf-8')
        fp.truncate()
        fp.close()
        stat_code = 'file_truncated'
        return stat_code
    else:
        raise FileNotFoundError('нет такого файла')
