import re


def second_input_finder_func(text_str: str, t_ch: str) -> int:
    """
    Поиско второго вхождения символа
    :param text_str: текстовая строка
    :param t_ch: искомый символ
    :return:  тндекст второго вхожденичя символа (счет с 0)
    >>> second_input_finder_func(text_str='sims', t_ch='s')
    sims
    3
    >>> second_input_finder_func(text_str='окко', t_ch='о')
    окко
    3

    """
    if isinstance(text_str, str) and isinstance(t_ch, str) and not any(i.isdigit() for i in text_str) and len(
            text_str) > 0 and t_ch != '':
        try:
            print(text_str)
            ind = [i.start() for i in re.finditer(t_ch, text_str)]
            return ind[1]
        except(ValueError, TypeError, IndexError):
            raise IndexError('проверьте ввод, возможно, слово содержит символ всего 1 раз')

    else:
        raise TypeError('Введите  непустую символьную строку и искомый символ, не равный пробелу (не цифру)')
