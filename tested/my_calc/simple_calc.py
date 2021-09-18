def counter(s: str, a: float, b: float) -> float:
    """
    Элеменгтарный калькулято ввод: зак операции, операнд1,операнд2

    :param s: знак операции
    :param a:  операнд1
    :param b:  операнд2
    :return:  результат операции

    >>> counter('-',2,1)
    1
    >>> counter('/',4,2)
    2.0
    >>> counter('+',5,3)
    8
    >>> counter('*',2,2)
    4




    """
    zn = '+ - * /'
    if s not in zn:
        raise ValueError('нет нужных знаков')

    if s in zn:
        try:
            if s == '+':
                return a + b
            elif s == '-':
                return a - b
            elif s == '*':
                return a * b
            elif s == '/' and b == 0:
                raise ZeroDivisionError('На ноль не делим ')
            elif s == '/' and b != 0:
                return a / b

        except(ValueError, TypeError):
            raise ValueError('Должен быть 1 знак и 2 целых числа')
