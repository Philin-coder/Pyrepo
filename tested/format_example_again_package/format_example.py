def format_example_func(start_int: int) -> str:
    """
    Иллюстрация работы с f- строкой
    :param start_int: анчальное значение
    :return: следующее и предыдущее число для него
    >>> format_example_func(start_int=4)
    The prev number for the number 3  next is 5 .
    The next number for the number 3 is 2 .
    'prev number for this  number  3 and next number for the number 5'


    """
    if isinstance(start_int, int):
        b = start_int - 1
        c = start_int + 1
        print("The prev number for the number", b, " next is", c, '.')  # print старый
        print("The next number for the number", b, "is", b - 1, '.')
        return f'prev number for this  number  {start_int - 1} and next number for the number {c}'
        # print новый, где f- фраза, а {b} и {c} - результирующие
    else:
        raise TypeError(f'Введите  целое число а не {type(start_int).__name__}')
