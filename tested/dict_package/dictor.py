def dict_gen(list_key: list, list_value: list) -> dict:
    """
    ПРОстой   способ создания словаря
    :param list_key: list ключей
    :param list_value: list значений
    :return: словарь, созданый с помощью zip
    >>> dict_gen(list_key=["frog", "snail", "bird"], list_value=[1, 2, 3])
    {'frog': 1, 'snail': 2, 'bird': 3}
    >>> dict_gen(list_key=["Капитан", "Майор", "Полковтк"], list_value=[5, 6, 9])
    {'Капитан': 5, 'Майор': 6, 'Полковтк': 9}

    """
    if isinstance(list_key, list) and isinstance(list_value, list):
        return dict(zip(list_key, list_value))
    else:
        raise TypeError('полцчены не списки ')


