def task(arr):
    p = []
    index = 0
    for a in arr:
        if a > 0:
            p.insert(index, a)
            index += 1
        else:
            p.append(a)
    return p
 
 
print(task([1, 4, -7, 0, 12, 5, -3]))