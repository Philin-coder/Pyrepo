def bubble_sort(n: int) -> list:
    """
    Пример сортировки пузырьком
    :param n: диапазон
    :return: отсортированный список
    >>> bubble_sort(n=10)
    [49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10]
    [22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 19, 16, 13, 10]

    """
    if isinstance(n, int):
        un_sorted_ints = []
        for i in (reversed(range(10, 50, 3))):
            un_sorted_ints.append(i)
        print(un_sorted_ints)
        i = 0
        while i < n - 1:
            j = 0
            while j < n - 1 - i:
                if un_sorted_ints[j] > un_sorted_ints[j + 1]:
                    un_sorted_ints[j], un_sorted_ints[j + 1] = un_sorted_ints[j + 1], un_sorted_ints[j]
                j += 1
            i += 1

        return un_sorted_ints
    else:
        raise TypeError('Ведите целое число')
