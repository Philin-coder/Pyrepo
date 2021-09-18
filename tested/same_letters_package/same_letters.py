def first_and_last_let_func(text_str: str) -> str:
    """
    Проверка совпадения первой и  последней буквы слова
    :param text_str: текстовая строка
    :return:  сообщение пользоватеою, о том, совпадают ли буквыы
    >>> first_and_last_let_func(text_str='окно')
    окно
    'первая и последняя буквы совпадают'
    >>> first_and_last_let_func(text_str='окна')
    окна
    'первая и последняя буквы не  совпадают'
    >>> first_and_last_let_func(text_str='ОкнО')
    ОкнО
    'первая и последняя буквы совпадают'

    """
    if isinstance(text_str, str) and len(text_str) > 0 and not any(i.isdigit() for i in text_str):
        print(text_str)
        if text_str[0] == text_str[len(text_str) - 1:]:
            return 'первая и последняя буквы совпадают'
        else:
            return 'первая и последняя буквы не  совпадают'
    else:
        raise TypeError('Введите непустую строку в нижнем или верхнем  регистре ')



