from bisect import insort
 
def insertionSorted(iterable, steps=3):
    it = iter(iterable)
    result = []
    for _, x in zip(range(steps + 1), it):
        insort(result, x)
    result.extend(it)
    return result
    
assert insertionSorted((8, 1, 7, 4, 3, 9, 2, 5, 6, 10)) == [1, 4, 7, 8, 3, 9, 2, 5, 6, 10]