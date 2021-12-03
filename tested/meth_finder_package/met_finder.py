def met_finder_func(meth: str) -> list:
    """
    Вывод методов объекта.
    :param meth: Имя объекта.
    :return: список методов объекта.
    """
    if isinstance(meth, str) and meth != '':
        meths = [i for i in dir(meth)]
        return meths
    else:
        raise TypeError('передан неверный тип данных')
