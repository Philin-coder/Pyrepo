class first:
    def mf(self):
        print('hello')
        for i in (dir(first)):
            print(i)


f = first()  # объект
f.mf()  # вызов метода
