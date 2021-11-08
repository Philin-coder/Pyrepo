import os


def cont_gen(text_str: str) -> str:
    """
    Генерация контента для записи в файл.
    :param text_str: Текстовая строка.
    :return: Данные, которые будут записаны в файл
    >>> cont_gen(text_str='просто данные')
    'просто данные'
    """
    if isinstance(text_str, str) and text_str != '':
        return text_str
    else:
        raise TypeError('Пeредан неверный тип данных.')


def write_to_file(my_filename: str, f_ext: str, fdata: str) -> str:
    """
    Запись данных в файл.
    :param my_filename: Имя файла.
    :param f_ext: Расширение .
    :param fdata: Записываемые данные.
    :return: код состояния(успешна ли запись).
    Образец вызова.
     write_to_file(my_filename='c_test', f_ext='txt', fdata=cont_gen(text_str='просто данные '))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(my_filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(fdata, file=fp, sep="\n")
        stat_code = 'file_created'
        return stat_code
    else:
        raise TypeError('Файл имеет неверный тип ')


def file_reader(my_filename: str, f_ext: str) -> list:
    """
    Чтение файла.
    :param my_filename:Имя файла.
    :param f_ext: Расширение.
    :return: Прочитанные данные.
    Образец вызова.
    file_reader(my_filename='c_test', f_ext='txt')
    ['просто данные \n']
    """
    if os.path.isfile(my_filename + '.' + f_ext):

        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = fp.readlines()
        return data
    else:
        raise FileNotFoundError('это не файл')


def sym_counter(c_data: list, ch: str) -> int:
    """
    Подсчет символов в файле(равных введенному).
    :param c_data: Считанные из файла данные.
    :param ch: Символ, количество которых подсчитывается.
    :return: Количество символов равных введенному в файле.
    Образец вызова.
    sym_counter(c_data=file_reader(my_filename='c_test', f_ext='txt'), ch='о')
    2
    """
    if isinstance(c_data, list) and len(c_data) != 0 and ch != '\n':
        k = 0
        for i in ''.join(c_data):
            if i.lower() == ch:
                k += 1
        return k
    else:
        raise TypeError('Передан не список, либо список пуст ')
