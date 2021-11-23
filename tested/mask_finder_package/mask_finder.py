import fnmatch
import os


def get_files(msk: str) -> list:
    """
    Поиск по маске с помощью fnmatch.
    :param msk: маска.
    :return: список файлов в текущей папке, подходящих под шаблон
    Образец вызова
    get_files(msk='*.py')
    """
    if isinstance(msk, str) and msk != '' and not any(i.isdigit() for i in msk):
        files = [i for i in os.listdir('.') if fnmatch.fnmatch(i, msk)]
        return files
    else:
        raise TypeError('Передан неверный тип данных')
