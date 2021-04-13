def starter(my_filename, fext2, mstr):
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(mstr, file=fp, sep="\n")


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)
    data = str(data)
    for i in data:
        data = data.replace(']', ' ')
        data = data.replace('[', ' ')
        data = data.replace('\'', ' ')
        data = data.replace('\\', ' ')
        data = data.replace('n', ' ')
    print(data)
    for i in data.split():
        if i.startswith("м"):
            print(i)


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    starter(my_filename='test', fext2='txt', mstr='мама мыла раму')
    reader(my_filename='test', fext2='txt')
