import json
import os


def cont_gen(text_str: str) -> str:
    """
    Генерация контента для записи в Json
    :param text_str: текстовая строка.
    :return: Данные, которые будут записаны в файла
    >>> cont_gen(text_str='to be writen in Json')
    'to be writen in Json'
    >>> data_convert(conv_data=cont_gen(text_str='to be writen in Json'))
    {'to': 'word', 'be': 'word', 'writen': 'word', 'in': 'word', 'Json': 'word'}
    >>> file_read(file_name='data', f_ext='json')
    {'to': 'word', 'be': 'word', 'writen': 'word', 'in': 'word', 'Json': 'word'}
    >>> as_str(f_data=file_read(file_name='data', f_ext='json'))
    'to  be  writen  in  Json'
    """
    if isinstance(text_str, str) and text_str != '':
        return text_str
    else:
        raise TypeError('Передан неверный тип данных, либо  - пустая строка')


def data_convert(conv_data: str) -> dict:
    """
    Конвертация данных в словарь.
    :param conv_data: исходная строка.
    :return: Словарь, полученный из этой строки.
    """
    if isinstance(conv_data, str) and conv_data != '':
        return dict.fromkeys(conv_data.split(), 'word')
    else:
        raise TypeError('Передан неверный тип данных')


def write_file(file_name: str, f_ext: str, f_data: dict) -> str:
    """
    Запись данных файл.
    :param f_data: данные, которе будут записаны в файл.
    :param file_name: Имя файла
    :param f_ext: Расширение.
    :return: Код состояния(успешна ли запись).
    """
    if isinstance(f_ext, str) and f_data == data_convert(conv_data=cont_gen(text_str='to be writen in Json')):
        with open(file_name + '.' + f_ext, 'w') as fp:
            json.dump(f_data, fp)
        stat_code = 'file_created'
        return stat_code

    else:
        ValueError('Передан неверный тип данных')


def file_read(file_name: str, f_ext: str) -> dict:
    """
    Чтение  файла
    :param file_name: имя файла.
    :param f_ext: Расширение.
    :return: Прочитанные данные.
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext) as fp:
            res = json.load(fp)
        return res

    else:
        raise FileNotFoundError('нет такого файла')


def as_str(f_data: dict):
    """
    Очистка результирующей строки.
    :param f_data: исходные данные(конвертированный в строку список ключей словаря).
    :return:строка.
    """
    if isinstance(f_data, dict):
        return str(f_data.keys()).removeprefix('dict_keys([').removesuffix('])').replace('\'', '').replace(',', ' ')
    else:
        raise TypeError('Передан неверный тип данных')
