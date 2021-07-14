def intersection(*arrays):
    res = set.intersection(*map(set, arrays))
    return list(res)
 
print(intersection([1, 2, 3], [101, 2, 1, 10], [2, 1]))