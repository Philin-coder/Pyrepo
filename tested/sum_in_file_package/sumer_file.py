import os


def range_gen(start_p: int, end_p: int) -> list:
    """
    Генерация списка чисел.
    :param start_p: начало диапазона.
    :param end_p: конец диапазона.
    :return: Результирующий список.
    >>> range_gen(start_p=1, end_p=10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    if isinstance(start_p, int) and isinstance(end_p, int) and start_p > 0 and end_p > 0:
        try:
            ints = [i for i in range(start_p, end_p + 1)]
            if all(isinstance(i, int) for i in ints):
                return ints
            else:
                raise TypeError('Передан неверный тип данных')

        except(TypeError, ValueError):
            raise TypeError('введите числа')
    else:
        raise TypeError('введите числа')


def str_maper(m_data: list) -> str:
    """
    Конвертация Списка в необходимый вид.
    :param m_data: Исходный список.
    :return: Он же, в виде строки.
    >>> str_maper(m_data=range_gen(start_p=1, end_p=10))
    '1 2 3 4 5 6 7 8 9 10'
    """
    if isinstance(m_data, list) and len(m_data) != 0:
        return str(m_data).strip().removeprefix('[').removesuffix(']').replace(',', '')
    else:
        raise TypeError('Передан неверный тип данных')


def file_writer(filename: str, f_ext: str, w_data: str) -> str:
    """
    Запись чисел в файл через строку.
    :param filename: Имя файла.
    :param f_ext: Расширение.
    :param w_data: Данные, которые должны быть записаны в файл.
    :return: Код состояния(успешна ли запись).
    >>> file_writer(filename='test', f_ext='txt', w_data=str_maper(m_data=range_gen(start_p=1, end_p=4)))
    'file_created'
    """
    if isinstance(f_ext, str) and f_ext == 'txt':
        with open(filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            fp.writelines('%s\n' % line for line in w_data)
            fp.close()
            stat_code = 'file_created'
            return stat_code
    else:
        raise TypeError('Файл имеет неверный тип')


def sum_ints_in_file(file_name: str, f_ext: str) -> int:
    """
    Суммирование чисел в файле.
    :param file_name: Имя файла
    :param f_ext: расширение
    :return: сумма чисел в файле.
    >>> sum_ints_in_file(file_name='test', f_ext='txt')
    10
    """
    if os.path.isfile(file_name + '.' + f_ext):
        with open(file_name + '.' + f_ext, 'r') as fp:
            return sum(map(int, fp.read().split()))
    else:
        raise FileNotFoundError('Это не файл')
