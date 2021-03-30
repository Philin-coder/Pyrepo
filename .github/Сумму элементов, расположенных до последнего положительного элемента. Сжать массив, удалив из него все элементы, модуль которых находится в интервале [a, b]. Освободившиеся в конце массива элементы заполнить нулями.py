def some1(lst):
    res = 0
    found = False
    for i in lst[::-1]:
        if found:
            res = res + i
        else:
            found = i > 0
    return res
 
 
def some2(lst, a, b):
    res = []
    for i in lst:
        if i < 0:
            i = -i
        if a < i and i > b:
            res.append(i)
    return res