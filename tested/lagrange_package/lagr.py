def lagrange(x: int, _pow: int, q: int) -> [int, str]:
    """
    Теорема Лагранжа о сумме четырёх квадратов гласит:

"Всякое натуральное число можно представить в виде суммы четырёх квадратов целых чисел."

 программа, которая по заданному числу "n", выведет от 1 до 4 натуральных чисел,
 квадраты которых дают в сумме данное число.
    :param x:первый квалрат
    :param _pow: второй
    :param q: третий
    :return:т 1 до 4 натуральных чисел, квадраты которых дают в сумме данное число
    >>> lagrange(28, 2, 4)
    '5 1 1 1'
    >>> lagrange(50, 2, 4)
    '7 1'

    """
    if isinstance(x, int) and isinstance(_pow, int) and isinstance(q, int):
        if _pow > 0:
            b = int(x ** (1 / _pow))
            if x - b ** _pow == 0:
                return str(b)
            if q == 1:
                return 0
            while lagrange(x - b ** _pow, _pow, q - 1) == 0:
                b -= 1
            if b <= 0:
                return 0
            return str(b) + ' ' + lagrange(x - b ** _pow, _pow, q - 1)
        else:
            raise ZeroDivisionError('Нельзя делить на 0')
    else:
        raise TypeError('Введите  целые числа ')
