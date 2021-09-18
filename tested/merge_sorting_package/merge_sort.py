def merge_sort_func(mixed_ints: list) -> tuple:
    """
    Иллюстрация сортировки слиянием
    :param mixed_ints: список не отсортрованных чисел
    :return:  кортеж  отсортрованных чисел
    >>> merge_sort_func(mixed_ints=[])
    Splitting  []
    ('Merging ', [])
    >>> merge_sort_func(mixed_ints=[54, 26, 93, 17, 77, 31, 44, 55, 20])
    Splitting  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Splitting  [54, 26, 93, 17]
    Splitting  [54, 26]
    Splitting  [54]
    Splitting  [26]
    Splitting  [93, 17]
    Splitting  [93]
    Splitting  [17]
    Splitting  [77, 31, 44, 55, 20]
    Splitting  [77, 31]
    Splitting  [77]
    Splitting  [31]
    Splitting  [44, 55, 20]
    Splitting  [44]
    Splitting  [55, 20]
    Splitting  [55]
    Splitting  [20]
    ('Merging ', [17, 20, 26, 31, 44, 54, 55, 77, 93])

    """
    if isinstance(mixed_ints, list):
        print("Splitting ", mixed_ints)
        if len(mixed_ints) > 1:
            mid = len(mixed_ints) // 2
            left_half = mixed_ints[:mid]
            right_half = mixed_ints[mid:]

            merge_sort_func(left_half)
            merge_sort_func(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    mixed_ints[k] = left_half[i]
                    i = i + 1
                else:
                    mixed_ints[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                mixed_ints[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                mixed_ints[k] = right_half[j]
                j = j + 1
                k = k + 1
        return "Merging ", mixed_ints

    else:
        raise TypeError(f'введите список, а не {type(mixed_ints).__name__}')
