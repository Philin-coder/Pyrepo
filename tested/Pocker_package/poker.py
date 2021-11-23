def check_combination(cards: list) -> str:
    """
    Даны 5 целых чисел. Среди них:
    * если одинаковы 5, то вывести "Impossible", иначе
    * если одинаковы 4, то вывести "Four of a Kind", иначе
    * если одинаковы 3 и 2, то вывести "Full House", иначе
    * если есть 5 последовательных, то вывести "Straight", иначе
    * если одинаковы 3, то вывести "Three of a Kind", иначе
    * если одинаковы 2 и 2, то вывести "Two Pairs", иначе
    * если одинаковы 2, то вывести "One Pair", иначе
    * вывести "Nothing".
    Входные данные
    В первой строке находятся 5 чисел через пробел. Все числа от 1 до 13 включительно.
    Выходные данные:
    Выводится одна строка - результат анализа.
    :param cards: список.
    :return: Результат анализа
    >>> check_combination([1, 1, 1, 1, 1])
    'Impossible'
    >>> check_combination([1, 1, 1, 1, 0])
    'Four of a Kind'
    >>> check_combination([1, 1, 1, 2, 2])
    'Full House'
    >>> check_combination([1, 2, 3, 4, 5])
    'Straight'
    >>> check_combination([1, 5, 3, 2, 4])
    'Straight'
    >>> check_combination([1, 1, 1, 2, 4])
    'Three of a Kind'
    >>> check_combination([1, 1, 2, 2, 4])
    'Two Pairs'
    >>> check_combination([1, 1, 2, 3, 4])
    'One Pair'
    >>> check_combination([1, 9, 2, 3, 4])
    'Nothing'
    """
    if isinstance(cards, list) and all(isinstance(i, int) for i in cards) and len(cards) != 0:
        minimal_value = min(cards)
        if sorted(cards) == list(range(minimal_value, minimal_value + 5)):
            return 'Straight'
        uniques = list(set(cards))
        uniques_length = len(uniques)
        if uniques_length == 1:
            return 'Impossible'
        if uniques_length == 4:
            return 'One Pair'
        if uniques_length == 2:
            if any(filter(lambda x: cards.count(x) == 4, uniques)):
                return 'Four of a Kind'
            else:
                return 'Full House'
        if uniques_length == 3:
            if any(filter(lambda x: cards.count(x) == 3, uniques)):
                return 'Three of a Kind'
            else:
                return 'Two Pairs'
        return 'Nothing'
    else:
        raise TypeError('передан неверный тип данных')
