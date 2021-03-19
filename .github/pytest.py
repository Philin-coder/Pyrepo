import random


def massgen(n):
    mlist = [random.uniform(-10.0, 100.9) for i in range(n)]
    print(*mlist)
    for i in mlist:
        if i>0:
            mlist.remove(i)
    print(mlist)




if __name__ == '__main__':
    massgen(n=3)
