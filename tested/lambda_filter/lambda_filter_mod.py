def list_filter_func(text_str: str) -> list:
    """
    Иллюстрация фильтра по списку
    :param text_str: ключ фильтрации
    :return: отфильтрованный список
    >>> list_filter_func(text_str='просо')
    ['просо', 'просо', 'просо', 'просо', 'просо']
    >>> list_filter_func(text_str='мак')
    ['мак', 'мак', 'мак', 'мак', 'мак']
    >>> list_filter_func(text_str='пшено')
    []

    """
    if isinstance(text_str, str) and not any(i.isdigit() for i in text_str):
        mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
        find_list = list(filter(lambda x: x == text_str, mixed))
        return find_list
    else:
        raise TypeError('Введите строку')
