class vklad:
    def __init__(self, fio, nomers, summav, god):
        self.fio = fio
        self.nomers = nomers
        self.summav = summav
        self.god = god

        def __repr__(self):
            return repr((self.fio, self.nomers, self.summav, self.god))

    def zap(self):

        vklader.append(self.fio)
        vklader.append(self.nomers)
        vklader.append(self.summav)
        vklader.append(self.god)

        with open(filename + '.' + fext2, 'w+', encoding='utf-8') as fp:
            print(vklader, file=fp, sep="\n")

            fp.close()

    def chten(self):
        with open(filename + '.' + fext2, 'r', encoding='utf-8') as fp:
            mlist = [line.strip() for line in fp]
            fp.close()
        mlist1 = sorted(mlist)
        a = mlist1
        for i in range(len(mlist1)):
            v = a[i]
            j = i
            while (a[j - 1] > v) and (j > 0):
                a[j] = a[j - 1]
                j = j - 1
                a[j] = v
            print(a)
            return a


if __name__ == '__main__':
    mlist = []
    vklader = []
    filename = 'rab'
    fext2 = 'txt'
    vk = vklad(fio=str(input("фио")), nomers=(int(input("счет"))), summav=float(input("вклад")), god=int(input("год")))
    vk.zap()
    vk.chten()
    vk1 = vklad(fio=str(input("фио")), nomers=(int(input("счет"))), summav=float(input("вклад")), god=int(input("год")))
    vk1.zap()
    vk1.chten()
