def masgen(my_filename, fext2,n):
    mlist = list(map(int, input().split()))
    res=[i for i in mlist if i % 2 != 0]
    print(res)
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(res, file=fp, sep="\n")
def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)
 
 
 
if __name__ == '__main__':
        my_filename = None
        fex2 = None
        masgen(my_filename='test', fext2='txt',n=5)
        reader(my_filename='test', fext2='txt')