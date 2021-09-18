import random


def alpha(n):
    for i in range(97, 123):
        print(chr(i))
        mlist.append(chr(i))
    print(mlist)
    mlist1 = [ chr(random.randint(97, 123)) for i in range(n)]
    return mlist1


if __name__ == '__main__':
    mlist = []

    print(alpha(n=int(input())))
