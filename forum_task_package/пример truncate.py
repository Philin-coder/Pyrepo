# todo: and me
def f_zap(my_filename, f_ext2):
    with open(my_filename + '.' + f_ext2, 'w', encoding='utf-8') as fp:
        print('проба', file=fp, sep="\n")
    fp = open('проба.txt', 'w')
    fp.truncate()
    fp.close()


# def reader(my_filename, f_ext2):
#     with open(my_filename + '.' + f_ext2, 'r', encoding='utf-8') as fp1:
#         data = [fp1.readline()]
#     print(data)


if __name__ == '__main__':
    f_zap(my_filename='проба', f_ext2='txt')
    # reader(my_filename='проба', f_ext2='txt')
