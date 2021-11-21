def min_max(arr: list) -> tuple:
    """
    Отыскание минимума и максимума.
    :param arr: исходный список.
    :return: минимум и максимум(кортеж).
    >>> min_max(arr=[1, 2, 3, 4, 5, 6])
    (1, 6)
    """
    if isinstance(arr, list) and all(isinstance(i, int) for i in arr) and len(arr) > 0:
        mi, ma = arr[0], arr[0]
        for a in arr[1:]:
            if a > ma:
                ma = a
            if a < mi:
                mi = a
        return mi, ma
    else:
        raise TypeError('передан неверный тип данных, либо пустой список')
