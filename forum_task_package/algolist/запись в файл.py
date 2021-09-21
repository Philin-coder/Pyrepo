my_filename = 'test'
f_ext2 = 'txt'
link_lis = []
with open(my_filename + '.' + f_ext2, 'w', encoding='utf-8') as fp:
    print(link_lis, file=fp, sep="\n")
