import os


def cont_gen(n: int) -> list:
    """
    Генерация контента для файла.
    :param n: диапазон чисел.
    :return: список чисел, соответствующий диапазону.
    Образец вызова cont_gen(n=8)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if isinstance(n, int) and n != 0 and n > 0:
        ints = list(range(1, n + 1))
        return ints
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(file_name: str, f_ext: str, f_data: list) -> str:
    """
    Запись в файл.
    :param file_name: иям файла
    :param f_ext: расширение.
    :param f_data: данные, которые будут записаны в файл..
    :return:
    Образец вызова  write_to_file(file_name='avg_file', f_ext='txt', f_data=cont_gen(n=8))
    'file_created'
    """
    if isinstance(file_name, str) and isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_data, file=fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('файл имеет неверный тип')


def read_from_file(file_name: str, f_ext: str) -> list:
    """
    Чтение из файла
    :param file_name: имя файлаю
    :param f_ext: расширение.
    :return: читаемые данные.
    Образец вызова  read_from_file(file_name='avg_file', f_ext='txt')
    ['[1, 2, 3, 4, 5, 6, 7, 8]\n']
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
            fdata = fp.readlines()
        return fdata
    else:
        raise FileNotFoundError('нет такого файла')


def conv_to_int(fdata: list) -> list:
    """
    Конвертация в числа, прочитанной строки.
    :param fdata: считанный список(строк)
    :return: список чисел
    Образец вызова conv_to_int(fdata=read_from_file(file_name='avg_file', f_ext='txt'))
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if isinstance(fdata, list) and fdata is not None:
        return list(map(int, ''.join(
            str(fdata).replace('\'', '').replace('\\n', ' ').replace(',', ' ').removesuffix(']').removesuffix(
                ']').removeprefix('[').removesuffix(']').replace(']', '').replace('[', '')).replace(' ', '')))
    else:
        raise TypeError('Передан неверный тип данных')


def avg_of_file(avg_data: list) -> float:
    """
    Вывод среднего.
    :param avg_data:исходный список.
    :return:среднее
    Образец вызова avg_of_file(avg_data=conv_to_int(fdata=read_from_file(file_name='avg_file', f_ext='txt')))
    4.5
    """
    if isinstance(avg_data, list) and all(isinstance(i, int) for i in avg_data):
        try:
            return sum(avg_data) / len(avg_data)
        except ZeroDivisionError:
            raise ZeroDivisionError('на ноль делить грешно ')

    else:
        raise TypeError('Передан неверный тип данных')
