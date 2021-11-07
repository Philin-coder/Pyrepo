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
    one_sym(my_filename='test', f_ext='txt')
   ['[', "'", 'A', 'V', ' ', 'i', 's', ' ', 'l', 'a', 'r', 'g', 'e', 's', 't', ' ', 'A', 'n', 'a',
   'l', 'y', 't', 'i', 'c', 's', ' ', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', ' ', 'o', 'f', ' ', 'I', 'n', 'd',
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
    ['', '', 'AV', '', 'is', '', 'largest', '', 'Analytics', '', 'community', '', 'of', '', 'India', '', 'n', '', '', '']
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
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'^\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def last_word_only(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\w+$', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def two_letters_from_begin_no_spaces(my_filename: str, f_ext: str) -> list:
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\w\w', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def two_letters_from_begin_no_spaces_as_word(my_filename: str, f_ext: str) -> list:
    if os.path.isfile(my_filename + '.' + f_ext):
        with open(my_filename + '.' + f_ext, 'r', encoding='utf-8') as fp:
            data = str(fp.readlines())
        return re.findall(r'\b\w.', data)
    else:
        raise FileNotFoundError('Файл имеет неверный тип ')


def dom_finder(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'@\w+.(\w+)', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def date_finder(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\d{2}-\d{2}-\d{4}', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def year_finder(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\d{2}-\d{2}-(\d{4})', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def vols_in_begin(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\b[aeiouAEIOU]\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def invert_search(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\b[^aeiouAEIOU]\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def invert_search_with_space(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\b[^aeiouAEIOU ]\w+', text_str)
    else:
        raise TypeError('Передана не строка, или-строка пуста')


def num_checker(nums: list) -> str:
    if isinstance(nums, list) and nums != []:
        for i in nums:
            if re.match(r'[8-9][0-9]{9}', i) and len(i) == 10:
                return 'yes'
            else:
                return 'no'
    else:
        raise TypeError('Передан не список , или-список пуст')


def str_cleaner(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.split(r'[;,\s]', text_str)
    else:
        raise TypeError('Передан неверный тип данных')


def str_cleaner_spaces(text_str: str) -> str:
    if isinstance(text_str, str) and text_str != '':
        return re.sub(r'[;,\s]', ' ', text_str)
    else:
        raise TypeError('Передан неверный тип данных')


def html_cleaner(text_str: str) -> list:
    if isinstance(text_str, str) and text_str != '':
        return re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', text_str)
    else:
        raise TypeError('Передан неверный тип данных')


if __name__ == '__main__':
    print(cont_gen(file_cont='AV is largest Analytics community of India'))
    # print(cont_gen(file_cont={'AV is  largest Analytics community of India.'}))

    print(write_to_file(file_name='r_test', f_ext='txt',
                        fdata=cont_gen(file_cont='AV is largest Analytics community of India')))

    # print(write_to_file(file_name='r_test', f_ext='tt',
    #                     fdata=cont_gen(file_cont='AV is largest Analytics community of India')))

    print(one_sym(my_filename='r_test', f_ext='txt'))
    # print(one_sym(my_filename='r_test', f_ext='tt'))

    print(one_letter(my_filename='r_test', f_ext='txt'))
    # print(one_letter(my_filename='r_test', f_ext='tt'))

    print(letters_with_spaces(my_filename='r_test', f_ext='txt'))
    # print(letters_with_spaces(my_filename='r_test', f_ext='tt'))

    print(letters_only(my_filename='r_test', f_ext='txt'))
    # print(letters_only(my_filename='r_test', f_ext='tt'))

    print(first_word_only(text_str='AV is largest Analytics community of India'))
    # print(first_word_only(text_str=123))

    print(last_word_only(text_str='AV is largest Analytics community of India'))
    # print(last_word_only(text_str=123))

    print(two_letters_from_begin_no_spaces(my_filename='r_test', f_ext='txt'))
    # print(two_letters_from_begin_no_spaces(my_filename='r_test', f_ext='tt'))

    print(two_letters_from_begin_no_spaces_as_word(my_filename='r_test', f_ext='txt'))
    # print(two_letters_from_begin_no_spaces_as_word(my_filename='r_test', f_ext='tt'))

    print(dom_finder(text_str='abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'))
    # print(dom_finder(text_str=123))

    print(date_finder(text_str='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'))
    # print(date_finder(text_str=''))

    print(year_finder(text_str='Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'))
    # print(year_finder(text_str=''))

    print(vols_in_begin(text_str='Task, is , very very, difficult to Me'))
    # print(vols_in_begin(text_str=''))

    print(invert_search(text_str='Task, is , very very, difficult to Me'))
    # print(invert_search(text_str=''))

    print(invert_search_with_space(text_str='AV is largest Analytics community of India'))
    # print(invert_search_with_space(text_str=''))
    print(num_checker(nums=['9999999999', '999999-999', '99999x9999']))
    print(num_checker(nums=['999999-999', '99999x9999']))
    print(num_checker(nums=['999999-999']))
    # print(num_checker(nums=[]))
    print(str_cleaner(text_str='no more;fake,snd,lie,for me'))
    # print(str_cleaner(text_str=''))

    print(str_cleaner_spaces(text_str='no more;fake,snd,lie,for me'))
    # print(str_cleaner_spaces(text_str=''))

    print(html_cleaner(text_str='1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'))
    # print(html_cleaner(text_str=''))
