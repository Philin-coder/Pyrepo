def str_comparer(text_str: str, fnd_str: str) -> str:
    """
    Поиск слова в строке
    :param text_str: текстовая строка
    :param fnd_str:  искомое слов
    :return: результат(в зависимости от того, есть ли слово в строке пользователь получает соответствующее сообщение )
    >>> str_comparer(text_str='Проба первая', fnd_str='Проба')
    'вторая строка есть в первой'
    >>> str_comparer(text_str='Проба первая', fnd_str='тут')
    'Нет второй строки в первой'

    """
    if isinstance(text_str, str) and isinstance(fnd_str, str) and not any(i.isdigit() for i in text_str) and not any(
            i.isdigit() for i in fnd_str) and len(text_str) > 0 and len(fnd_str) > 0:
        for i in range(len(text_str) - len(fnd_str) + 1):
            if fnd_str == text_str[i:i + len(fnd_str)]:
                return 'вторая строка есть в первой'
            else:
                return 'Нет второй строки в первой'
    else:
        raise TypeError('Введите 2 непустых  строки, не содержащих чисел')
