import os


def gen_cont_file(data_str: [str, int]) -> [str, int]:
    """
    Формирование контента файла.
    :param data_str: текстовая строка.
    :return:Строка, которая будет записана в файл.
    >>> gen_cont_file(data_str='проба')
    'проба'
    """

    if data_str is not None and data_str != '':
        return data_str
    else:
        raise TypeError('Передан неверный  тип данных')


def write_to_file(file_name: str, f_ext: str, fdata: str) -> str:
    """
    Запись контента в файл.
    :param file_name: имя файла.
    :param f_ext: Расширение.
    :param fdata: Данные, которе будут записаны в файл.
    :return: код состояния(успешна ли запись)
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(fdata, file=fp, sep="\n")
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверное расширение')


def file_reader(file_name: str, f_ext: str) -> list:
    """
    Чтение файла.
    :param file_name: имя файла.
    :param f_ext: Расширение.
    :return: данные, которые были в файле.
    """

    if os.path.isfile(file_name + '.' + f_ext):
        try:
            with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
                data = fp.readlines()
            return data
        except FileNotFoundError:
            raise FileNotFoundError('Файл не найден')
    else:
        raise FileNotFoundError('это  не файл')
