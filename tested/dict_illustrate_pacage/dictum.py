def dict_func() -> str:
    """
    Иллюстрация работы функции  zip
    :return: результат поиска по ключу
    >>> dict_func()
    'Лена живет в  городе Обнинск'

    """
    friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
    friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
    friends = dict(zip(friends_names, friends_cities))
    return f'Лена живет в  городе {friends["Лена"]}'
