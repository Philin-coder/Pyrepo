def finder(text_str: str, n: int) -> str:

    """
    :param text_str: текстовая строка
    :param n: номер слова в строке
    :return: выбраное слово, наоборот(счет с 0)
    >>> finder(text_str='мама мыла раму', n=1)
    мама мыла раму
    'алым'
    >>> finder(text_str='ratio ergo sum', n=2)
    ratio ergo sum
    'mus'
    >>> finder(text_str='В четверг, четвертого числа', n=1)
    В четверг, четвертого числа
    ',гревтеч'




    """

    if isinstance(text_str, str) and isinstance(n, int) and len(text_str) > 1:
        print(text_str)
        res = text_str.split()
        ind_list = [res.index(i) for i in res]
        for i in ind_list:
            if i == n:
                return res[i][::-1]
    else:
        raise TypeError('Введите строку, затем - целое число')



