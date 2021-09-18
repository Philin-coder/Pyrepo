n = int(input())
h = n // 60
m = n % 60
if h >= 24:
    h2 = h % 24
    print(h2, m)
else:
    print(h)
    print(m)
