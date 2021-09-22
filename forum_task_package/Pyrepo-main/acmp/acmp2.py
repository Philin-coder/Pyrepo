
with open('input.txt', 'r', encoding='utf-8') as fp:
    data = int(fp.readline())
    res = sum([i for i in range(1, data + 1)])
    res = str(res)
with open('output.txt', 'w', encoding='utf-8') as fp:
    print(res, file=fp)
