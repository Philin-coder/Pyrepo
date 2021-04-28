def zapis(my_filename, fext2,n):
    mdict=dict([input().split() for i in range(n)])
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(mdict, file=fp)


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)



if __name__ == '__main__':
    my_filename =''
    fex2 = ''
    zapis(my_filename='проба', fext2='txt',n=4)
    reader(my_filename='проба', fext2='txt')
