
d = dict()
for _ in range(int(input())):
    s = input()
    d[s] = d.get(s, 0) + 1
a = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
print(*a[:20])