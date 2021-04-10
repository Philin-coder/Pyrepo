n,m = map(int, input().split()) #кол-во участников и фиксаций
dn = {i: 0 for i in range(1, n+1)}
k = 1
x = list(map(int,input().split())) 
win = x[0]
for i in x:
    dn[i] += 1
    if dn[i] == k:
        k += 1
        win = i
print(win)