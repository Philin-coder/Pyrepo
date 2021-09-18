import collections


def str_conv_func(input_string: str, repl_string: str) -> str:
    """
    Замена букв на их количество в строке
    :param input_string: входная текстовая строка
    :param repl_string: строка, которая является результирующей
    :return:  строка, в которй буквы замененын на их количество(строка начинается с @)
    >>> str_conv_func(input_string='google', repl_string='@')
    '@2g 2o 1l 1e '
    >>> str_conv_func(input_string='Проба', repl_string='@')
    '@1П 1р 1о 1б 1а '
    >>> str_conv_func(input_string='Peple', repl_string='#')
    '#2e 1P 1p 1l '

    """
    if isinstance(input_string, str) and len(
            input_string) > 0 and input_string != '' and repl_string != '' and isinstance(repl_string, str):
        pass
        d = collections.defaultdict(int)
        for i in input_string:
            d[i] += 1
        for i in sorted(d, key=d.get, reverse=True):
            repl_string += '%d%s ' % (d[i], i)
        return repl_string
    else:
        raise TypeError('Введите непустую строку')


