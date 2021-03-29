lst = [1, 1, 1, 1, 0, 2, 2, 2, 0][::-1]
print(sum(lst[lst.index(0):lst.index(0, lst.index(0) + 1)]))