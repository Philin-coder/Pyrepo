a = input()

i = len(a)
k = 0
ii = i
w = 0

ifKit = False
p = []
for char in a:
    p.append(char)

for z in range(i - 1, 0, -1):
    w += int(p[z])
p.append(w)
w = 0
while k < int(a) + 1:
    for q in range(ii, ii - i, -1):
        w += int(p[q])

        if w == a:
            ifKit = True
    p.append(w)
    w = 0
    ii += 1
    k = p[ii]

if not ifKit:
    print("NO")
else:
    print("YES")