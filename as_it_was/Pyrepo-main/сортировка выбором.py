def vsort(arr):
    i = 0
    while (i < len(arr)):
        mi = arr[i]
        ii = i
        for j in range(i + 1, len(arr)):
            if arr[j] < mi:
                ii = j
                mi = arr[j]
        arr[i], arr[ii] = arr[ii], arr[i]
        i += 1


x = [1, 2, 3, 1, 2, 3, 1, 2, -6, 4, 1]
vsort(x)
print(x)
