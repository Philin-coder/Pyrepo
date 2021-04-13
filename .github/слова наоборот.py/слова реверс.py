a = list(map(str, input().split()))
temp = []
temp_num = 0
for i in range(len(a)):
    temp = list(a[i])
    temp = temp[::-1]
    temp_num = ''.join(temp)
    a[i] = temp_num
for i in range(len(a)):
    temp = list(a[i])
    for j in range(len(temp)): # ошибка на этом цикле выскакивает.
        if temp[j] == '0':
            temp.remove(temp[j])
    a[i] = ''.join(temp)
a = a[::-1]
ans = ''
for row in a:
    ans += row
    ans += ' '
print(ans)