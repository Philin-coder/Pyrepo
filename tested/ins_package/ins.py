import inspect
import re


def inspect_func(arg1, arg2):
    """
    Демонстрация функционала inspect
    :param arg1:первый  аргумент анализируемой функии
    :param arg2: второй  аргумент анализируемой функии
    :return: результат работы анализируемой функии
    >>> inspect_func(2, 3)
    5
    """
    if isinstance(arg1, int) and isinstance(arg2, int):
        return arg1 + arg2
    else:
        raise TypeError('Введите числа, в качестве аргументов')


def view_f(func):
    """
    Собственнно, inspect
    :param func: анализзируемая функия
    :return:  ее текст
    """
    return re.findall(r'\w+', inspect.getsource(func))


if __name__ == '__main__':
    print(inspect_func(2, 3))
    # print(inspect_func('2', '3'))
    print(view_f(inspect_func))
