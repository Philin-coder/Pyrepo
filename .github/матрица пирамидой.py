n = int(input())
j = 1
while j < n + 1:
    st = '  '*(n-j)
    i = j + 1
    while i > 1:
        i -= 1
        st += ' ' + str(i)
    while i < j:
        i += 1
        st += ' ' + str(i)
    j += 1
    print(st)
