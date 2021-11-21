import glob


def mask_finder(text_str: str) -> list:
    """
    Поиск файлов по маске.
    :param text_str: маска.
    :return: список найденных файлов
    Образец вызова
    mask_finder(text_str='./*.py')
    """
    if isinstance(text_str, str) and text_str != '':
        return glob.glob(text_str)
    else:
        raise TypeError('Передан неверный тип данных, либо - пустая строка')
