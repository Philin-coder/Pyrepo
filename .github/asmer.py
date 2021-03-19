my_filename = str(input("имя файла"))
data = str(input("что в файле"))
fext2 = 'txt'
print(my_filename)
with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
    print(data, file=fp, sep="\n")
    fp.close()
