import re
import os
import wikipedia


def cont_gen(title_str: str) -> str:
    """
    Генерация контента для записи в файл(загрузка статьи из wikipedia).
    :param title_str: тема статьи.
    :return: контент статьи.
    Образец вызова
    cont_gen(title_str='Python')
    """
    if isinstance(title_str, str) and title_str != '':
        return str(wikipedia.page(title_str).content)
    else:
        raise TypeError('Передан неверный тип данных, или -пустая строка')


def write_to_file(file_name: str, f_ext: str, f_data: str) -> str:
    """
    Запись данных в файл
    :param file_name: иям файла.
    :param f_ext: Расширение.
    :param f_data: записываемые данные.
    :return: Код состояния(успешна ли запись).
    Образец вызова.
    write_to_file(file_name='wiki2', f_ext='txt', f_data=cont_gen(title_str='PYTHON'))
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-16') as fp:
            fp.write(f_data)
            fp.close()
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')


def read_file(file_name: str, f_ext: str) -> str:
    """
    Чтение файла.
    :param file_name:Имя файла
    :param f_ext: Расширение.
    :return: Прочитанные данные.
    Образец вызова
    read_file(file_name='wiki2', f_ext='txt')
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r', encoding='utf-16') as fp:
            res = fp.readline()
            fp.close()
            return str(res)
    else:
        raise FileNotFoundError('нет такого файла')


def searcher(work_str: str) -> str:
    """
    Обработка строки регулярными выражениями.
    :param work_str: входная строка.
    :return: результат обработки.
    Образец вызова
    searcher(work_str=read_file(file_name='wiki2', f_ext='txt'))
    """
    if isinstance(work_str, str) and work_str != '':
        rx = re.sub("^(.+{}.+)$".format(re.escape(work_str.strip())), '', work_str, flags=re.MULTILINE)
        return re.sub(r'\n\s*\n', '\n', rx, re.MULTILINE)
    else:
        raise TypeError('Передан неверный тип данных, или -пустая строка')


def res_writer(file_name: str, f_ext: str, f_data: str) -> str:
    """
    Запись информации в файл.
    :param file_name: выражениями файла.
    :param f_ext: расширение
    :param f_data: записываемые данные
    :return: код состояния(успешна ли запись)
    Образец вызова
    res_writer(file_name='res', f_ext='txt', f_data=searcher(work_str=read_file(file_name='wiki2', f_ext='txt')))
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-16') as fp:
            print(f_data, file=fp)
            stat_code = 'file_created'
            return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')
