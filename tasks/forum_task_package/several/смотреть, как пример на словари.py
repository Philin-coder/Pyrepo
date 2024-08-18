# s=int(input("сколько раз вывести"))
def slov():
    mydict = {}
    # mydict=mydict.fromkeys(['name','sername'])
    mydict[str(input('Имя '))] = str(input("Фамилия"))

    print(mydict)
    print(mydict.keys())
    print(mydict.values())
    print(mydict.get('Иван'))
    mydict.clear()
    print(mydict)


if __name__ == '__main__':
    slov()
