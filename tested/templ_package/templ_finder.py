import os


def file_finder_func(text_str: str) -> list:
    """
    Иллюстрация поиска по маске
    :param text_str: шаблон
    :return: список имен файлов, которые под него подходят, если файлов нет, вернет пустой список
    >>> file_finder_func(text_str='rar')
    []

    """
    if isinstance(text_str, str):
        name_list = [i for i in (os.listdir(os.getcwd())) if i.endswith(text_str)]

        return name_list
    else:
        raise TypeError('Введена не строка')
