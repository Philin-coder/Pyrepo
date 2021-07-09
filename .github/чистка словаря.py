# Написать программу учета указаний сверху Программа учитывает
# новые указания и удаляет выполненные.
def dictgen():
    mdict = dict([input('введите ключ и значение через пробел').split()
                 for i in range(3)])
    print(mdict)
    mdict = {key: val for key, val in mdict.items() if val != 'выполнено'}
    return mdict


if __name__ == '__main__':

    print(dictgen())
