from collections import Counter
import os


def cont_gen(start_p: int, end_p: int, num) -> list:
    """
    Генерация частотности.
    :param start_p: начало диапазона
    :param end_p: конец диапазона.
    :param num: номер буквы
    :return: список букв, в которой заданная буква повторена дважды.
    >>> cont_gen(start_p=97, end_p=123, num=10)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'kk']
    """
    if isinstance(start_p, int) and isinstance(end_p,
                                               int) and start_p > 0 and end_p > 0 and start_p != 0 and end_p != 0:
        letters = [chr(i) for i in range(start_p, end_p)]
        dbl_let = [i * 2 for i in letters if letters.index(i) == num]
        letters.extend(dbl_let)
        return letters
    else:
        raise TypeError('Передан неверный тип данных')


def data_conv_str(letters: list) -> str:
    """
    Конвертация полученного списка букв в строку(убрав пробелы)
    :param letters: список букв.
    :return: Результирующая строка.
    >>> data_conv_str(letters=cont_gen(start_p=97, end_p=123, num=10))
    'abcdefghijklmnopqrstuvwxyzkk'
    """
    if isinstance(letters, list) and len(letters) != 0:
        return ''.join(
            str(list(map(str, letters))).strip().removeprefix('[').removesuffix(']').replace(',', '').replace('\'',
                                                                                                              '')). \
            replace(' ', '')
    else:
        raise TypeError('Передан не список, либо,-список пуст')


def write_file(filename: str, f_ext: str, fdata: str) -> str:
    """
    Запись в файл
    :param filename: Имя файла.
    :param f_ext: Расширение
    :param fdata: Данные, которе отправятся в файл
    :return: Код  состояния(успешна ли запись).
    >>> write_file(filename='com_test', f_ext='txt',
    ...                      fdata=data_conv_str(letters=cont_gen(start_p=97, end_p=123, num=10)))
    'file_created'

    """

    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(fdata, file=fp)
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')


def most_common_sym(filename: str, f_ext: str) -> Counter:
    """
    Чтение  и частотный анализ файла.
    :param filename: Имя файла.
    :param f_ext: Расширение.
    :return: Каких символов и сколько в файле.
    >>> most_common_sym(filename='com_test', f_ext='txt')
    Counter({'k': 3, 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1})
    """
    if os.path.isfile(filename + '.' + f_ext):
        with open(filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            c = Counter()
            for x in fp:
                c += Counter(x.strip())
        return c
    else:
        raise FileNotFoundError('Такого файла нет ')
