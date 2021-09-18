n = int(input())
s = [[]]

for i in range(n - 1):
    s.append([int(j) for j in input().split()])

station = input().split()
a, a1 = int(station[0]), int(station[1])

wl = s[max(a, a1)][min(a, a1)]
b = -1

for i in range(n):
    if i != a and i != a1:
        if wl > s[max(a, i)][min(a, i)] + s[max(i, a1)][min(i, a1)]:
            wl = s[max(i, a1)][min(i, a1)] + s[max(i, a1)][min(i, a1)]
            b = i

if b != -1:
    print(b)
else:
    print(a)
