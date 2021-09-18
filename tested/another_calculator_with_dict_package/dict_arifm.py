def counter_again(a: int, b: int, operation: str) -> [int, float]:
    """
    Еще один калькулятор
    :param a: операнд1
    :param b: операнд2
    :param operation:  знак операции
    :return: результат операции
    >>> counter_again(a=1, b=2, operation='+')
    3
    >>> counter_again(a=7, b=1, operation='-')
    6
    >>> counter_again(a=8, b=2, operation='*')
    16
    >>> counter_again(a=8, b=2, operation='/')
    4.0

    """
    signatures = ('+', '-', '*', '/')
    if operation not in signatures:
        raise ValueError('Нужных знаков нет')
    if isinstance(a, float) or isinstance(b, float) or isinstance(a, int) or isinstance(b, int) and isinstance(
            operation, str) and any(i in operation for i in signatures):
        try:
            count_dict = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y
            }
            if operation == '+':
                return count_dict['+'](a, b)
            elif operation == '-':
                return count_dict['-'](a, b)
            elif operation == '*':
                return count_dict['*'](a, b)
            elif operation == '/':
                if b == 0:
                    raise ZeroDivisionError('На ноль делить грешно')
                else:
                    return count_dict['/'](a, b)
        except(TypeError, ValueError):
            raise TypeError('Неверно введен тип операнда')
