def simple_add_example_func(x: [int, float], y: [int, float]) -> [int, float]:
    """
    Простой пример сложения чисел
    :param x: Первое числов
    :param y: ворое чмсло
    :return: резултат их сложения
    >>> simple_add_example_func(x=2, y=3)
    5
    >>> simple_add_example_func(x=5, y=5)
    10
    >>> simple_add_example_func(x=5, y=2.5)
    7.5

    """
    if isinstance(x, int) or isinstance(y, int) or isinstance(x, float) or isinstance(y, float):
        try:
            return x + y
        except TypeError:
            raise TypeError('введите 2 числа')
