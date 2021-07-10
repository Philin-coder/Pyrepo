n, k = map(int, input().split())

b = [0]*n

x = 1

t = 0

while k >= (n-t-1) and k > 0:
    k = k-(n-t-1)
    b[t] = n-t
    t += 1
    for i in range(-(n-t), 0):
        if i != -(k+1):
            b[i] = x
            x += 1
        else:
            b[i] = n-t
    print(*b)
