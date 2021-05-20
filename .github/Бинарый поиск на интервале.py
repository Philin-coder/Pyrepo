def bin_search(arr, k):
    mid = len(arr) // 2  # центр. элемент
    low = 0  # первый элемент массива
    high = len(arr) - 1  # последний элемент массива

    while arr[mid] != k and low <= high:
        if k > arr[mid]:  # сравнение значения среднего элемента с ключом поиска
            # сдвиг границ просматриваемой последовательности
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return []
    else:
        r = []
        i = mid
        while(arr[i] == k and i >= 0):
            r = [i]+r
            i -= 1
        i = mid+1
        while(arr[i] == k and i < len(arr)):
            r = r+[i]
            i += 1
        return r


x = [1, 2, 5, 7, 11, 11, 11, 23, 23, 23, 46, 47, 48]

print(bin_search(x, 23))
