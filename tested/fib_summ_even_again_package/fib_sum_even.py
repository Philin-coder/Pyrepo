def fib_sum_even_func(previous: int, next_: int) -> int:
    """
    Сумма четных числе Фибаначчи на интервале до 4000000
    :param previous: гачало вычислений
    :param next_: шаг цикла
    :return: сумма четных на интервале
    >>> fib_sum_even_func(previous=0,next_=1)
    4613732
    >>> fib_sum_even_func(previous=1,next_=5)
    16019504
    >>> fib_sum_even_func(previous=8,next_=10)
    4749426
    >>> fib_sum_even_func(previous=0,next_=10)
    5142270

    """
    if isinstance(previous, int) and isinstance(next_, int) and previous >= 0 and next_ > 0:
        result = 0
        while result < 4000000:
            previous, next_ = next_, previous + next_
            if not next_ % 2:
                result += next_
        return result
    else:
        raise TypeError('Введите целые положительные числа больше 0(шаг) для параметра начала исчисления и шага')
