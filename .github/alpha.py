import random


def alpha(n):
    for i in range(1040, 1072):
        print(chr(i))
        mlist.append(chr(i))
    print(mlist)
    mlist1 = [chr(random.randint(1040, 1072)) for i in range(n)]
    print(mlist1)
    for i in range(n):
        print(random.choice(mlist1))

    


if __name__ == '__main__':
    n = int(input())
    mlist = []

    alpha(n)
