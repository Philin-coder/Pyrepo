import random


def finder(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(mlist)
    mlist1 = []
    for i in mlist:
        if mlist.count(i) > 1 and i not in mlist1:
            print(i)
            mlist1.append(i)
    print(mlist1)


if __name__ == '__main__':
    n = int(input())
    finder(n)
