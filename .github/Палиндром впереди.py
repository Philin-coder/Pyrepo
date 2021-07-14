a = ['dfdg', 'aa', 'fgf', 'g', 'gt']
def fun(word): return word != word[::-1]


a.sort(key=fun)
print(a)
