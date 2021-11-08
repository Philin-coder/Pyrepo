import re
import os


def cont_gen(file_cont: str) -> str:
    """
     Генерация контента для записи  данных в файл.
    :param file_cont: текстовая строка.
    :return: Текстовая строка, котоая будет записаны в файл.
    >>> cont_gen(file_cont='AV is largest Analytics community of India')
    'AV is largest Analytics community of India'
    """
    if isinstance(file_cont, str) and file_cont != '':
        return file_cont
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(file_name: str, f_ext: str, fdata: str) -> str:
    """
    Запись данных в файл.
    :param file_name: Имя файла.
    :param f_ext: Расширение.
    :param fdata: Данные, котоая будут записаны в файл.
    :return: Код состояния(успешна ли запись).
    >>> write_to_file(file_name='r_test', f_ext='txt',
    ...                         fdata=cont_gen(file_cont='AV is largest Analytics community of India'))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(file_name + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(fdata, file=fp)
            stat_code = 'file_created'
            return stat_code
    else:
        raise ValueError('Файл имеет неправильный тип ')


def one_sym(my_filename: str, f_ext: str) -> list:
    """
    Обработка регулярными выражениями файла.
    :param my_filename: Имя файла.
    :param f_ext: расширение.
    :return: Результат извлечения из текста в файле всех символов.
    Образец вызова.
    one_sym(my_filename='r_test', f_ext='txt')
   ['[', "'", 'A', 'V',' ', 'i', 's',' ', 'l', 'a', 'r', 'g', 'e', 's', 't',' ', 'A', 'n', 'a',
   'l', 'y', 't', 'i', 'c', 's',' ', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y',' ', 'o', 'f',' ', 'I', 'n', 'd',
   'i', 'a', '\\', 'n', "'", ']']
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'.', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def one_letter(my_filename: str, f_ext: str) -> list:
    """
    Обработка регулярными выражениями файла.
    :param my_filename: Имя файла.
    :param f_ext: расширение.
    :return: Результат извлечения из текста в файле всех букв.
    Образец вызова.
    one_letter(my_filename='test', f_ext='txt')
    ['A', 'V', 'i', 's', 'l', 'a', 'r', 'g', 'e', 's', 't', 'A', 'n', 'a', 'l', 'y', 't', 'i', 'c',
    's', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', 'o', 'f', 'I', 'n', 'd', 'i', 'a', 'n']
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\w', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def letters_with_spaces(my_filename: str, f_ext: str) -> list:
    """
    Обработка регулярными выражениями файла.
    :param my_filename: Имя файла.
    :param f_ext: расширение.
    :return:  Результат извлечения из текста в файле всех букв м пробелов
    Образец вызова.
    letters_with_spaces(my_filename='test', f_ext='txt')
    ['', '', 'AV', '', 'is', '', 'largest', '', 'Analytics', '', 'community', '', 'of', '', '
    India', '', 'n', '', '', '']
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\w*', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def letters_only(my_filename: str, f_ext: str) -> list:
    """
    Обработка регулярными выражениями файла.
    :param my_filename: Имя файла.
    :param f_ext: Расширение.
    :return: Результат извлечения из текста в файле только  букв.
    Образец вызова.
    letters_only(my_filename='test', f_ext='txt')
    ['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India', 'n']
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\w+', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def first_word_only(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строкаа.
    :return: Результат обработки(поиска первого слова строки).
    >>> first_word_only(text_str='AV is largest Analytics community of India')
    ['AV']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'^\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def last_word_only(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: Исходный строка
    :return: Результат обработки(поиска последнего  слова строки)
    >>> last_word_only(text_str='AV is largest Analytics community of India')
    ['India']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\w+$', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def two_letters_from_begin_no_spaces(my_filename: str, f_ext: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param my_filename: Имя файла
    :param f_ext: Расширение.
    :return: результат извлечения из файла двух первых букв каждого слова.
    Образец вызова.
    two_letters_from_begin_no_spaces(my_filename='r_test', f_ext='txt')
    ['AV', 'is', 'la', 'rg', 'es', 'An', 'al', 'yt', 'ic', 'co', 'mm', 'un', 'it', 'of', 'In', 'di']
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\w\w', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def two_letters_from_begin_no_spaces_as_word(my_filename: str, f_ext: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param my_filename:имя файла.
    :param f_ext: Расширение.
    :return: результат извлечения из файла двух первых букв каждого слова(границы слова).
    Образец вызова.
    two_letters_from_begin_no_spaces_as_world(my_filename='r_test', f_ext='txt')
    ['AV', 'is', 'la', 'An', 'co', 'of', 'In', "n'"]
    """
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\b\w.', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def dom_finder(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: домены ииз этой строки.
    >>> dom_finder(text_str='abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
    ['com', 'in', 'com', 'biz']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'@\w+.(\w+)', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def date_finder(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: результат обработки(поиск даты).
    >>> date_finder(text_str='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
    ['12-05-2007', '11-11-2011', '12-01-2009']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\d{2}-\d{2}-\d{4}', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def year_finder(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: Исходная строка.
    :return: поиск года в ней.
    >>> year_finder(text_str='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
    ['2007', '2011', '2009']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\d{2}-\d{2}-(\d{4})', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def vols_in_begin(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: Результат обработки(слова, начинающиеся на гласную)
    >>> vols_in_begin(text_str='Task, is , very very, difficult to Me')
    ['is']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\b[aeiouAEIOU]\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def invert_search(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: Результат обработки(Инверсия поиска).
    >>> invert_search(text_str='Task, is , very very, difficult to Me')
    ['Task', 'very', ' very', 'difficult', ' to', ' Me']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\b[^aeiouAEIOU]\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def invert_search_with_space(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: Результат обработки(Инверсия поиска с учетом пробелов).
    >>> invert_search_with_space(text_str='AV is largest Analytics community of India')
    ['largest', 'community']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\b[^aeiouAEIOU ]\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def num_checker(nums: list) -> str:
    """
    Работа со списком.
    :param nums: исходный список.
    :return: является ли содержимое списка телефонным номером.
    >>> num_checker(nums=['9999999999', '999999-999', '99999x9999'])
    'yes'
    >>> num_checker(nums=['999999-999', '99999x9999'])
    'no'
    >>> num_checker(nums=['999999-999'])
    'no'
    """
    if isinstance(nums, list) and nums != []:
        for i in nums:
            if re.match(r'[8-9][0-9]{9}', i) and len(i) == 10:
                return 'yes'
            else:
                return 'no'
    else:
        raise TypeError('Передан не список , или-список пуст')


def str_cleaner(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: Результат обработки(убраны все разделители).
    >>> str_cleaner(text_str='no more;fake,snd,lie,for me')
    ['no', 'more', 'fake', 'snd', 'lie', 'for', 'me']
    """
    if isinstance(text_str, str) and text_str != '':
        return re.split(r'[;,\s]', text_str)
    else:
        raise TypeError('Передан неверный тип данных')


def str_cleaner_spaces(text_str: str) -> str:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return: Результат обработки(убраны все разделители, включая пробелы).
    >>> str_cleaner_spaces(text_str='no more;fake,snd,lie,for me')
    'no more fake snd lie for me'
    """
    if isinstance(text_str, str) and text_str != '':
        return re.sub(r'[;,\s]', ' ', text_str)
    else:
        raise TypeError('Передан неверный тип данных')


def html_cleaner(text_str: str) -> list:
    """
    Обработка строки регулярными выражениями.
    :param text_str: исходная строка.
    :return:Получение Текста.
    >>> html_cleaner(text_str='1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily')
    [('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'), ('Ethan', 'Mia'), ('Michael', 'Emily')]
    """
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', text_str)
    else:
        raise TypeError('Передан неверный тип данных')
