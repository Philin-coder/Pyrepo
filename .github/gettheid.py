import random


def get_the_id(n):
    mlist = list(random.randint(1, 10)for i in range(n))
    print(*mlist)
    print(mlist[0])
    print(id(mlist[0]))



if __name__ == '__main__':
    get_the_id(n=12)
