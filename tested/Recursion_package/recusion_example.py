def factorial_iterative_func(num: int) -> [tuple, str]:
    """
    Пример рекурсии
    :param num: целое число
    :return: факториал числа, добытый рекурисвноо
    >>> factorial_iterative_func(num=3)
    'Факториал 3 это 6'
    >>> factorial_iterative_func(num=-3)
    'Факториал не вычисляется для отрицательных чисел'
    """
    if isinstance(num, int):
        try:
            factorial = 1
            if num < 0:
                return f"Факториал не вычисляется для отрицательных чисел"
            else:
                for i in range(1, num + 1):
                    factorial = factorial * i
                return f"Факториал {num} это {factorial}"

        except(TypeError, ValueError):
            raise ValueError('введено отрицательное чичло')
    else:
        raise TypeError('Введите число')
