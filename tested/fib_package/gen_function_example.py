def fibonacci(a: int, b: int, mx: int) -> list:
    while a < mx:
        yield a
        a, b = b, a + b


def gen_start(a: int, b: int, mx: int) -> int:
    """
    Числа Фибаначии  генератор -функцией
    :param a:начальное значение функции генератора
    :param b: шаг генератора
    :param mx: максимальное значение
    :return:  сумма четных чисел Фибаначии на интервале до мx
    >>> gen_start(a=0, b=1, mx=4000000)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
    4613732
    >>> gen_start(a=1, b=2, mx=10)
    [1, 2, 3, 5, 8]
    10
    >>> gen_start(a=4, b=7, mx=33)
    [4, 7, 11, 18, 29]
    22
    >>> gen_start(a=0, b=0, mx=0)
    []
    0

    """
    if isinstance(a, int) and isinstance(b, int) and isinstance(mx, int) and a >= 0 and b >= 0 and mx >= 0:
        gen = fibonacci(a, b, mx)
        fib_lst = [i for i in gen]
        print(fib_lst)
        even_fib = [i for i in fib_lst if i % 2 == 0 and i < mx]
        return sum(even_fib)
    else:
        raise TypeError(
            'Введите положительные целые числа для шага генератора, максимума, генератора и начального значения генератора')
