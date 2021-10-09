def odd_even_func(a: int, b: int) -> dict:
    """
    Проверка четнсти чисел на интервале  при помощи & (побитового  AND)
    :param a:начало диапазона
    :param b:конец диапазона
    :return:словарь, с числами и их  четностью
    >>> odd_even_func(a=1, b=8)
    {1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True}
    """
    if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0:
        return dict(zip((i for i in range(a, b + 1)), (i & 1 != 1 for i in range(a, b + 1))))
    else:
        raise TypeError('Введите целые положительные числа')
