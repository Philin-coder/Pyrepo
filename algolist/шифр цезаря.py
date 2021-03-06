def ave(l, mstr):
    for i in mstr:
        mlist.append(alpha[(alpha.find(i) + l) % len(alpha)])
    print('Result: ', '"', ''.join(mlist), '"', sep='')


if __name__ == '__main__':
    l = int(input())
    mstr = input()
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    mlist = []
    ave(l, mstr)
