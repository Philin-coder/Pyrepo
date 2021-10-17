from bisect import bisect_left


def binary_search(a, x, lo=0, hi=None):
    """
    Модуль bisect - обеспечивает поддержку списка в отсортированном порядке с помощью алгоритма деления пополам.

Набор функций:

bisect.insort(list, elem), он же bisect.insort_right(list, elem) - вставка элемента в отсортированный список, при этом
elem располагается как можно правее (все элементы, равные ему, остаются слева).

bisect.insort_left(list, elem) - вставка элемента в отсортированный список, при этом elem располагается как можно левее
(все элементы, равные ему, остаются справа).

bisect.bisect(list, elem), он же bisect.bisect_right(list, elem) - поиск места для вставки элемента в отсортированный
список, таким образом, чтобы elem располагался как можно правее.

bisect.bisect_left(list, elem) - поиск места для вставки элемента в отсортированный список, таким образом, чтобы elem
располагался как можно левее.

Для полного счастья не хватает только функции для проверки наличия элемента в отсортированном списке. К счастью,
это легко решаемо.
    :param a:список
    :param x:искомый элемент
    :param lo:нижняя граница
    :param hi:верхняняя граница
    :return: позиция(по индексу) искомого элемента
    >>> binary_search(a=[1, 2, 3, 4, 5], x=5, lo=2)
    4
    >>> binary_search(a=[1, 2, 3, 4, 5], x=2, lo=5)
    -1
    >>> binary_search(a=[1, 2, 3, 4, 5], x=2, lo=2)
    -1
    >>> binary_search(a=[1, 2, 3, 4, 5], x=4, lo=2, hi=None)
    3
    >>> binary_search(a=[1, 2, 3, 4, 5], x=4, lo=2, hi=4)
    3

    """
    if isinstance(a, list) and isinstance(x, int) and isinstance(lo, int):
        hi = hi if hi is not None else len(a)
        pos = bisect_left(a, x, lo, hi)
        return pos if pos != hi and a[pos] == x else -1
    else:
        raise TypeError('передан невереый тип данных')
