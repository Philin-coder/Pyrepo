def porc_func(uni_ints: list, p: float) -> list[int]:
    """
    Отыскаине процентили
    :param uni_ints: исходный список чисел
    :param p: количество сходных результатов
    :return: процентиль
    Пример вызова
    print(porc_func(uni_ints=[random.randint(1, 10) for i in range(10)], p=random.uniform(0, 1)))
    """
    if isinstance(p, float) and isinstance(uni_ints, list) and all(isinstance(i, int) for i in uni_ints) and len(
            uni_ints) != 0:
        uni_ints = sorted(uni_ints)
        return uni_ints[int(round(p * len(uni_ints) + 0.5)) - 1]
    else:
        raise TypeError('передан неверный тип данных')
