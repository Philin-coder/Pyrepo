def replacer_func(comp: str, names: list) -> list:
    """
    Иллюстрация замены строк при помощи генератора
    :param comp: значения, на которе заменяем слово КОМПАНИЯ
    :param names: на что заменяем
    :return: результирующий список

    """
    if isinstance(comp, str) and isinstance(names, list):
        return [str.replace(comp, "КОМПАНИЯ", c) for c in names]
    else:
        raise TypeError('Передан невернвйй тип даннных')
