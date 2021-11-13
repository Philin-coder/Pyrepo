import os


def to_cript_word(text_str: str) -> str:
    """
    Данные для записи в файл.
    :param text_str: текстовая строка.
    :return: Данные, которое будут записаны в файл.
    >>> to_cript_word(text_str='ave cezar')
    'ave cezar'
    """
    if isinstance(text_str, str) and text_str != '' and all([isinstance(i, str) for i in text_str]):
        return text_str
    else:
        raise TypeError('Передан неверный тип данных')


def write_file(file_name: str, f_ext: str, f_fdata: str) -> str:
    """
    Запись данных в файл.
    :param file_name: Имя файла.
    :param f_ext: Расширение.
    :param f_fdata: Данные, которое будут записаны в файл.
    :return: Код состояния(успешна ли запись).
    Образец вызова.
    print(write_file(file_name='to_cript_text', f_ext='txt', f_fdata=to_cript_word(text_str='ave cezar')))
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_fdata, file=fp)
            stat_code = 'file_created'
            return stat_code
    else:
        raise ValueError('Файл имеет неверный тип')


def file_read(file_name: str, f_ext) -> str:
    """
    Чтение файла.
    :param file_name: имя файла.
    :param f_ext: расширение.
    :return: прочитанные данные.
    Образец вызова.
    print(file_read(file_name='to_cript_text', f_ext='txt'))
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
            res = fp.readlines()
            return str(res).removeprefix('[', ).removesuffix(']').strip().replace('\'', '').replace('\\n', ' ')
    else:
        raise FileNotFoundError('нет такого файла')


def cesar_encode(line: str, shift: int) -> str:
    """
    Шифрование данных Шифром Цезаря.
    :param line: шифруемая строка.
    :param shift: шаг шифра.
    :return: Зашифрованная строка.
    Образец вызова.
    print(cesar_encode(line=file_read(file_name='to_cript_text', f_ext='txt'), shift=1))
    """
    if isinstance(line, str) and isinstance(shift, int) and line != '' and shift > 0 and shift != 0:
        result = ''
        for letter in line:
            if letter.isalpha():
                number = ord(letter) + shift % 32
                if number > 1103:
                    number -= 32
                result += chr(number)
            else:
                result += letter
        return result
    else:
        raise TypeError('Передан неверный тип данных, или неверный диапазон шага')
