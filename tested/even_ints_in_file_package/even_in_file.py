def even_cont_gen(n: int) -> list:
    """
    Генерация списка четных чисел.
    :param n: Числовой диапазон.
    :return: результирующий список.
    >>> even_cont_gen(n=12)
    [2, 4, 6, 8, 10, 12]
    """
    if isinstance(n, int) and n > 0 and n != 0:
        even_ints = [i for i in range(1, n + 1) if i % 2 == 0]
        return even_ints
    else:
        raise TypeError('Передан неверный тип данных')


def write_to_file(filename: str, f_ext: str, f_data: list) -> str:
    """
    запись четных(парных) чисел в файл
    :param filename: Имя файла.
    :param f_ext: расширение файла.
    :param f_data:Записываемые данные
    :return: код состояния(успешна ли запись).
    >>> write_to_file(filename='test', f_ext='txt', f_data=even_cont_gen(n=12))
    'file_created'
    """

    if isinstance(f_ext, str) and isinstance(f_data, list) and f_ext == 'txt' and all(
            isinstance(i, int) for i in f_data):
        with open(filename + '.' + f_ext, 'w', encoding='utf-8') as fp:
            print(f_data, file=fp, sep='\n')
        stat_code = 'file_created'
        return stat_code
    else:
        raise ValueError('Файл имеет неверное расширение, или получен неверный тип данных')

