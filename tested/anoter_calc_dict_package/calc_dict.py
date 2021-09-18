def dict_count_func(x: float, y: float, key_to_find: str) -> [int, float]:
    """
    Калькулятор работающмй на основе словаря
    :param x:  первый операнд
    :param y: второй операнд
    :param key_to_find:  код операции
    :return: резульат операции
    >>> dict_count_func(x=2, y=5, key_to_find='add')
    7
    >>> dict_count_func(x=2, y=5, key_to_find='sub')
    -3
    >>> dict_count_func(x=2, y=5, key_to_find='mul')
    10
    >>> dict_count_func(x=2, y=5, key_to_find='div')
    0.4

    """
    operations = ('add', 'sub', 'mul', 'div')
    if isinstance(x, float) and isinstance(y, float) or isinstance(x, int) or isinstance(y, int) and any(
            i in key_to_find for i in operations):

        try:
            m_count_dict = {
                'add': lambda a, b: a + b,
                'sub': lambda a, b: a - b,
                'mul': lambda a, b: a * b,
                'div': lambda a, b: a / b

            }
            if key_to_find == 'add':
                return m_count_dict['add'](x, y)
            elif key_to_find == 'sub':
                return m_count_dict['sub'](x, y)
            elif key_to_find == 'mul':
                return m_count_dict['mul'](x, y)
            elif key_to_find == 'div':
                if y == 0:
                    raise ZeroDivisionError('на ноль делить -Зло ')
                else:
                    return m_count_dict['div'](x, y)
        except(TypeError, ValueError):
            raise TypeError(
                'введите 2 числа и код операции(add- сложение, sub- вычитание, mul-умножене, div- деленеи)')
        else:
            raise ValueError('неверно введен код операции')
