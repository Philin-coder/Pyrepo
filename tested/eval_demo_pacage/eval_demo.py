def eval_demo_func(x: int) -> int:
    """
    иллюстрация eval

    :param x: входной параметр
    :return:  результат подсчета
    >>> eval_demo_func(x=12)
    248832

    """
    if isinstance(x, int):
        return eval(f'{str(x)}**5')
    else:
        raise TypeError('введите число')
