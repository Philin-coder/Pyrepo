def file_write(file_name: str, fext: str, full_names: list) -> str:
    """
    Запись в файл.
    :param file_name: имя файла.
    :param fext:  расширение.
    :param full_names: записываемые данные
    :return: код состояния(успешна ли запись)
    """
    if isinstance(fext, str) and fext == 'txt' and isinstance(full_names, list) and full_names is not None:
        with open(file_name + '.' + fext, 'w', encoding='utf-8') as fp:
            print(full_names, file=fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise TypeError('Передан неверный тип данных, ли -пустой список')


def file_read(file_name: str, f_ext: str) -> list:
    """
    Чтение файла
    :param file_name: имя файла.
    :param f_ext: Расширение.
    :return: прочитанные данные.
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
            res = fp.readlines()
        return res
    else:
        raise ValueError('Файл имеет неверный тип')


def name_searcher(file_name: str, fext: str) -> str:
    """
    Поиск имен  в файле.
    :param file_name: имя файла.
    :param fext: Расширение
    :return: Результат поиска.
    """
    if isinstance(fext, str) and fext == 'txt':
        with open(file_name + '.' + fext, 'r', encoding='utf-8') as fp:
            data = fp.read().splitlines()
            phone_book = {}
            end_name = []
            for line in data:
                _name = list(filter(lambda x: x.isalpha() or x == ' ', line))
                number = line[len(_name):]
                _name = ''.join(_name).strip()
                phone_book[_name] = number
                end_name.append(line)
            return str(end_name).strip().removesuffix(']').removeprefix('[').replace('\'', ' ').replace(',',
                                                                                                        '').strip().replace(
                '\"', '').removeprefix('[').removesuffix(']')
    else:
        raise FileNotFoundError('нет такого файла')
