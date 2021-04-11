arr=list(map(int,input().split()))
pl = len(arr) // 2
res = [a + b for a, b in zip(arr[:pl], reversed(arr[pl:]))]
if pl + pl != len(arr):
    res.append(arr[pl])
print(res)
