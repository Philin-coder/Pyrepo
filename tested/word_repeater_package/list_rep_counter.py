def list_rep_counter_func(wordlist: list) -> dict:
    """
    Количество повторов в списке
    :param wordlist: анализируемый список
    :return: количество повторов в нем(словарь)

    """
    if isinstance(wordlist, list) and len(wordlist) > 0 and not any(i.isdigit() for i in wordlist):
        print(*wordlist)
        return dict((i, wordlist.count(i)) for i in set(wordlist) if wordlist.count(i) > 1)
    else:
        raise TypeError('передан неверный тип данных')
