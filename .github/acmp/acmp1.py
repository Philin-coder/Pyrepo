with open('input.txt', 'r', encoding='utf-8') as fp:
    data = fp.readline()
    res = (int(data.split()[0]) + int(data.split()[1]))
with open('output.txt', 'w', encoding='utf-8') as fp:
    print(res, file=fp, sep="\n")
