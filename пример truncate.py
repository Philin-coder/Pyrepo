def zapis(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print('проба', file=fp, sep="\n")
    fp = open('проба.txt', 'w')
    fp.truncate()
    fp.close()


# def reader(my_filename, fext2):
#     with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp1:
#         data = [fp1.readlines()]
#     print(data)


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    zapis(my_filename='проба', fext2='txt')
    reader(my_filename='проба', fext2='txt')
