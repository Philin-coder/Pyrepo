def sl():
    pools = [tuple(pool) for pool in alph.split()] * povt
    res = [[]]
    for pool in pools:
        res = [x + [y] for x in res for y in pool]
    for prod in res:
        print(''.join(tuple(prod)))
    print('итого', len(res))


if __name__ == '__main__':
    alph = input('введите буквы без пробела')
    povt = int(input('сколько букв'))
    sl()
