import os


def gen_cont(text_str: str) -> str:
    """
    Генерация записываемого в файл контента.
    :param text_str: Текстовая строка.
    :return: Текстовая строка, которая будет записана в файл
    >>> gen_cont('yes')
    'yes'
    """
    if isinstance(text_str, str) and text_str != '':
        return text_str
    else:
        raise TypeError('Передан неверный тип данных, либо-пустая строка')


def file_write(file_name: str, f_ext: str, fdata: str) -> str:
    """
    Создание файла
    :param file_name: Имя файла.
    :param f_ext: Расширение.
    :param fdata: данные, которые будет записаны в файл.
    :return:  код состояния(успешна ли запись).
    >>> file_write('n_test', f_ext='txt', fdata=gen_cont('yes'))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(fdata, file=fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('файл имеет неверный тип')


def file_reader(file_name: str, f_ext: str) -> str:
    """
    Чтение файла.
    :param file_name: Имя файла.
    :param f_ext: расширение.
    :return: Считанные из файла данные(в виде строки)
    >>> file_reader(file_name='n_test', f_ext='txt')
    'yes '
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r') as fp:
            fdata = fp.readlines()
        return str(fdata).strip().removesuffix(']').removeprefix('[').replace('\'', ''). \
            replace('\\', ' ').replace('n', '')
    else:
        raise FileNotFoundError('это не файл')
