def euclidean_distance_func(v1: list, v2: list) -> [float, int]:
    """
    евклидово расстояние между объектами
    :param v1: списоок координат первого объекта
    :param v2: списоок координат второго  объекта
    :return: Edrkbljdj расстояние между объекьаит
    >>> euclidean_distance_func(v1=[12.0, 11.0, 2], v2=[11.0, 9.0, 1.0])
    2.449489742783178
    >>> euclidean_distance_func(v1=[12.0], v2=[11.0])
    1.0
    >>> euclidean_distance_func(v1=[12.0], v2=[11.0, 1112, 4])
    1.0

    """
    if isinstance(v1, list) and isinstance(v2, list) and not any(isinstance(i, str) for i in v1) and not any(
            isinstance(i, str) for i in v2):
        return sum((x - y) ** 2 for x, y in zip(v1, v2)) ** 0.5
    else:
        raise TypeError('передан неверный тип данных')
