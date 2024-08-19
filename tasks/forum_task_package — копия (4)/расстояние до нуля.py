a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] != 0:
        b = [a[:i + 1], a[i:]]
        b[0] = list(reversed(b[0]))
        left = len(a) + 1
        right = len(a) + 1
        for j in range(len(b[0])):
            if b[0][j] == 0:
                left = j
                break
        for k in range(len(b[1])):
            if b[1][k] == 0:
                right = k
                break
        a[i] = min(left, right)
    print(a)
