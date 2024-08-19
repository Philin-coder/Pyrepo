import collections

emp = [
    ['Иванов', '11.05.1985', 5, 20000],
    ['Петров', '15.09.1985', 8, 25000],
    ['Сидоров', '8.07.1987', 3, 23000],
    ['Дубов', '11.07.1983', 7, 25000]
]
k = 3

grouped = collections.defaultdict(list)
for item in emp:
    grouped[item[1][-4:]].append(item)

for a, gr in grouped.items():
    i = ''
    for e in gr:
        if e[2] > k:
            if i != a: print(a)
            print(' ', e[0])
            i = a
