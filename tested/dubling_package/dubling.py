def repeat_func(n: int, text_str: str) -> str:
    """
        Даны натуральное число n, символы s1, …, sn. Преобразовать последовательность,
        удалив каждый символ «–» и повторив каждый символ,
        отличный от «-».

        :param n: длинна строки
        :param text_str:  строка
        :return: результирующая строка
        >>> repeat_func(n=3, text_str='s-s')
        's, s, s, s'
        >>> repeat_func(n=3, text_str='---')
        ''
        >>> repeat_func(n=3, text_str='мир')
        'мир'
        """
    if isinstance(n, int) and isinstance(text_str, str):
        if len(text_str) == n:
            allowed = '-'
            if any(i in text_str for i in allowed):
                text_str = text_str.replace('-', '')
                return str([i for i in text_str * 2]).removeprefix('[').removesuffix(']').replace('\'', '')
            elif not any(i in text_str for i in allowed):
                return text_str
        else:
            raise ValueError("строка должна быть нужной длинны")
    else:
        raise TypeError('Введите  длинну строки, затем -саму строку')
