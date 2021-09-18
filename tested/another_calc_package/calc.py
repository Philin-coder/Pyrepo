def calculate(operation: str, a: int, b: int) -> [int, float]:
    """
    Простой калькулятор
    :param operation: операция
    :param a:операнд 1
    :param b:операнд 2
    :return: результат
    >>> calculate(operation='+', a=2, b=3)
    5
    >>> calculate(operation='-', a=6, b=2)
    4
    >>> calculate(operation='/', a=18, b=2)
    9.0
    >>> calculate(operation='*', a=8, b=2)
    16
    """
    if isinstance(operation, str) and isinstance(a, int) and isinstance(b, int):
        operations = ('+', '-', '*', '/')
        if operation not in operations:
            raise ValueError('Нужных знаков нет ')
        if operation in operation:
            try:
                count_dict = {
                    '+': lambda x, y: a + b,
                    '-': lambda x, y: a - b,
                    '*': lambda x, y: a * b,
                    '/': lambda x, y: a / b
                }
                if operation == '+':
                    return count_dict['+'](a, b)
                elif operation == '-':
                    return count_dict['-'](a, b)
                elif operation == '*':
                    return count_dict['*'](a, b)
                elif operation == '/':
                    if b == 0:
                        raise ZeroDivisionError('на ноль не делим ')
                    else:
                        return count_dict['/'](a, b)

            except(ValueError, TypeError):
                raise ValueError('Должен быть 1 знак и 2 целых числа')
    else:
        raise TypeError('введите  код операции, затем 2 числа')
