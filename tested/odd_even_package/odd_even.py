def count_even_odd_func(n: int) -> tuple:
    """
    Получение четных и нечетных чисела на интервале
    :param n: целок чмсло
    :return: 2 списка : четные и нечетыные числа интервала
    >>> count_even_odd_func(n=12)
    ('чет[2, 4, 6, 8, 10, 12]', 'нечет[1, 3, 5, 7, 9, 11]')
    >>> count_even_odd_func(n=13)
    ('чет[2, 4, 6, 8, 10, 12]', 'нечет[1, 3, 5, 7, 9, 11, 13]')
    >>> count_even_odd_func(n=0)
    ('чет[]', 'нечет[]')
    >>> count_even_odd_func(n=1)
    ('чет[]', 'нечет[1]')
    >>> count_even_odd_func(n=2)
    ('чет[2]', 'нечет[1]')



    """
    if isinstance(n, int):
        return f'чет{[i for i in range(1, n + 1) if not i % 2]}', f'нечет{[i for i in range(1, n + 1) if i % 2]}'
    else:
        raise TypeError('Введите  целое число')


if __name__ == '__main__':
    print(count_even_odd_func(n=12))
    print(count_even_odd_func(n=13))
    print(count_even_odd_func(n=0))
    # print(count_even_odd_func(n='0'))
