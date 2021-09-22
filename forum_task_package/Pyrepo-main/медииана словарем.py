k = {'d': 25.4, "v": 44.5, "m": 1000, "s": 10, "f": 304.8}
n = int(input())
man = []
for i in range(n):
    man.append(input().split())
    man[i][1] = int(man[i][1]) * k[man[i][2]]
print(man[next(i for i, (_, x, __) in enumerate(man) if x == (min([man[i][1] for i in range(len(man))],
                                                                  key=lambda num: abs(num - sum(
                                                                      [man[i][1] for i in range(len(man))]) / len(
                                                                      man)))))][0])
