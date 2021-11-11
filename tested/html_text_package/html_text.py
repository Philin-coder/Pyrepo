import requests
from requests.exceptions import HTTPError
import os


def get_content(m_html: str) -> str:
    """
    Получение текста html-страницы.
    :param m_html: web-адрес.
    :return: текст страницы.
    Образец вызова
    get_content(m_html='https://ya.ru/')
    """
    if isinstance(m_html, str):
        try:
            code = requests.get(m_html)
            code.raise_for_status()
            return str(code.content)
        except HTTPError as http_err:
            raise f'HTTP error occurred: {http_err}'
        except Exception as err:
            raise f'Other error occurred: {err}'

    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(file_name: str, f_ext: str, f_data: str) -> str:
    """
    Запись данных в файл.
    :param file_name: имя файла.
    :param f_ext: расширение.
    :param f_data: данне для записи.
    :return: клд состояния(успешна ли запись).
    Образец вызова.
    write_to_file(file_name='html_text', f_ext='txt',
                        f_data=get_content(m_html='https://ya.ru/'))
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_data + '.' + f_ext, file=fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('файл имеет неверный тип')


def read_from_file(file_name: str, f_ext: str) -> str:
    """
    Чтение файла.
    :param file_name: имя файла.
    :param f_ext: Расширение.
    :return: Читаемые данне.
    Образец вызова
    read_from_file(file_name='html_text', f_ext='txt')
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
            f_data = fp.readlines()
            return str(f_data)
    else:
        raise FileNotFoundError('Такого файла нет')
