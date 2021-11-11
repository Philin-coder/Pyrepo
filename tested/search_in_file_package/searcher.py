import re
import wikipedia
import os


def cont_gen(title_pages: str) -> str:
    """
    Получение статью на заданную тему из wikipedia, отобрать все слова, выбрать самое большое число в статье.
    :param title_pages: тема статьи.
    :return: контент статьи.
    Образец вызова
    cont_gen(title_pages='Facebook')
    """
    if isinstance(title_pages, str) and title_pages != '':
        return wikipedia.page(title_pages).content
    else:
        raise TypeError('передан неверный тип данных,либо -пустая строка')


def write_to_file(file_name: str, f_ext: str, f_data: str) -> str:
    """
    Запись информации в файл.
    :param file_name: имя файла.
    :param f_ext: расширение.
    :param f_data: данные, которые будут записаны в файл.
    :return: Код состояния(успешна ли запись)
    Образец вызова
    write_to_file(file_name='wiki_test', f_ext='txt', f_data=cont_gen(title_pages='Facebook'))
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_data, file=fp)
            stat_code = 'file_created'
            return stat_code
    else:
        raise ValueError('файл имеет неверный тип')


def file_reader(file_name: str, f_ext: str) -> list:
    """
    Чтение файла.
    :param file_name: имя файла.
    :param f_ext: расширение
    :return: данные, считанные из файла.
    Образец вызова
    file_reader(file_name='wiki_test', f_ext='txt')
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
            return fp.readlines()
    else:
        raise FileNotFoundError('нет такого файла')


def wordfinder(conv_data: list) -> list:
    """
    Поиск всех слов, содержащихся в файле.
    :param conv_data: содержимое текстового файла.
    :return: Только слова, содержащиеся в данном файле
    Образец вызова
    wordfinder(conv_data=file_reader(file_name='wiki_test', f_ext='txt'))
    """
    if isinstance(conv_data, list) and len(conv_data) != 0:
        return re.findall(r'\b\w+', str(conv_data).removeprefix('[').removesuffix(']').strip())
    else:
        raise TypeError('Передан неверный тип данных, либо - пустой список')


def max_digit_finder(conv_data: list) -> int:
    """
    Поиск максимального числа, в файле.
    :param conv_data: вся информация, содержащаяся в файле.
    :return: Максимальное число, содержащееся в файле.
    Образец вызова
    max_digit_finder(conv_data=file_reader(file_name='wiki_test', f_ext='txt'))
    """
    if isinstance(conv_data, list) and len(conv_data) != 0:
        return max(list(map(int, re.findall(r'\d+', str(conv_data).removeprefix('[').removesuffix(']').strip()))))
    else:
        raise TypeError('Передан неверный тип данных, либо - пустой список')
