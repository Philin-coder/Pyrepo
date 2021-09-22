t = r'''easy = 2 + 2
if easy       == 4:# А вдруг нет?
    print('Квадрат с обрезанными углами:')
    print('/-\\')
    print('|#|')
    a =      '       ', 0
    print('\\_/')
    print('0\'1')#000'''

res = []
for l in t.split('\n'):
    i = 0
    try:
        # ^\s+
        while True:
            if l[i] != ' ':
                break
            res.append(l[i])
            i += 1
        while True:
            # начало строки
            if l[i] == "'":
                # '.*'
                res.append(l[i])
                i += 1
                while True:
                    # экранируем
                    if l[i] == '\\':
                        res.append(l[i])
                        i += 1
                        res.append(l[i])
                        i += 1
                        continue
                    # rjytw cnhjrb
                    if l[i] == "'":
                        res.append(l[i])
                        i += 1
                        break
                    res.append(l[i])
                    i += 1
                continue
            if l[i] == ' ':
                res.append(l[i])
                i += 1
                while l[i] == ' ':
                    i += 1
                continue
            if l[i] == '#':
                break
            res.append(l[i])
            i += 1
        # it is all
    except IndexError:
        pass
    res.append('\n')
print(''.join(res))
