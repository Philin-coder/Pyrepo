import re
import wikipedia


def zapis(mstr, my_filename, fext2):
    cont = wikipedia.page(mstr)
    res = cont.content
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(res, file=fp, sep="\n")
    return res


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)


def wordfinder(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
        data = str(data)
        wl = sorted(re.findall(r'\b\w+', data), key=lambda x: len(x), reverse=True)
        for i in wl:
            if len(i) == len(wl[0]):
                print(i)


def digitfinder(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
        data = str(data)
        mlist = [re.findall(r'\d+', data)]
        print(mlist)
        map(int, mlist)
        print(*mlist)
        print(max(*mlist))


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    zapis(mstr='Facebook', my_filename='проба', fext2='txt')
    reader(my_filename='проба', fext2='txt')
    wordfinder(my_filename='проба', fext2='txt')
    digitfinder(my_filename='проба', fext2='txt')
