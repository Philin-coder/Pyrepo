# import random


def test(n):
    # mlist = [random.randint(1, 100) for i in range(n)]
    mlist = list(map(int, input().split()))
    print(*mlist)
    print(*list(set(mlist)))


if __name__ == '__main__':
    test(n=5)
