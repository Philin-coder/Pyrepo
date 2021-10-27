def t_clock_func(time_s: int) -> tuple:
    """
    Сколько часов, минут, секунд в заданном промежутке времени.
    :param time_s: целое число.
    :return: количство часов, минут, секунд
    >>> t_clock_func(time_s=3682)
    ('часов 1', 'минут1', 'секунд22 ')


    """
    if isinstance(time_s, int) and time_s > 0:
        return f'часов {time_s // 3600}', f'минут{(time_s - (time_s // 3600) * 3600) // 60}', f'секунд{time_s % 60} '
    else:
        raise TypeError('Ведите целое, положительное число ')
