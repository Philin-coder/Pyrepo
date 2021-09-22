from itertools import permutations
als = 'abcdefghijklmnopqrstuvwxyz'.upper()
st = input()
P = st.split(' ')
N = int(P[0])
M = int(P[1])
K = int(P[2])
als = als[1:N]
ls = []
s = ''
f = ''
for j in range(0, M + 1):
    for i in permutations('A' * j + als * (M - j), M):
        if str(i) not in s:
            for k in i:
                f += k
            ls.append(f)
            f = ''
            s += str(i)
print(sorted(ls)[K - 1] if (K - 1) < len(ls) else 'None')