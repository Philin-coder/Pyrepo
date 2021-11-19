import json
import os


def cont_gen(text_str: str) -> str:
    """
    Генерация контента для файла.
    :param text_str: текстовая строка.
    :return: Данные, готовые для записи в файл.
    >>> cont_gen(text_str='text string')
    'text string'
    """
    if isinstance(text_str, str):
        return text_str
    else:
        raise TypeError('передан неверный тип данных, либо - пустая строка')


def conv_data(text: str) -> dict:
    """
    Конвертация контента в словарь.
    :param text:исходная строка.
    :return:словарь, готовый для записи в файла.
    >>> conv_data(text=cont_gen(text_str='text string'))
    {'text': 'word', 'string': 'word'}

    """
    if isinstance(text, str) and text != '':
        return dict.fromkeys(text.split(), 'word')
    else:
        raise TypeError('передан неверный тип данных, либо - пустая строка')


def write_file(filename: str, fdata: dict) -> str:
    """
    Запись в файл.
    :param filename: имя файла.
    :param fdata: данные, для записи в файл.
    :return: код состояния(успешна ли запись)
    >>> write_file(filename='data1.json', fdata=conv_data(text=cont_gen(text_str='text string')))
    'file_created'
    """
    if isinstance(fdata, dict) and isinstance(filename, str) and filename != '' and filename.endswith('.json'):
        with open(filename, 'w') as fp:
            json.dump(fdata, fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')


def read_file(filename: str) -> dict:
    """
    Чтение файла.
    :param filename: имя  файла.
    :return: Прочитанные данные.
    >>> read_file(filename='data1.json')
    {'text': 'word', 'string': 'word'}
    """
    if isinstance(filename, str) and filename != '' and os.path.isfile(filename):
        with open(filename) as fp:
            res = json.load(fp)
            return res
    else:
        raise FileNotFoundError('нет такого файла')


def as_it_was(fdata: dict) -> [str, list]:
    """
    Конвертация в исходный формат строка.
    :param fdata: Прочитанные данные(словарь).
    :return: Строка, в исходном виде.
    >>> as_it_was(fdata=read_file(filename='data1.json'))
    'text, string'
    """
    if isinstance(fdata, dict):
        return str(list(map(str, fdata.keys()))).replace('\'', '').removesuffix(']').removeprefix('[')
    else:
        raise TypeError('Передан неверный тип данных')


