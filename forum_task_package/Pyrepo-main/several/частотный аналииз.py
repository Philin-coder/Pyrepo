import random
from collections import Counter


def find_common(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(mlist)
    print(Counter(mlist).most_common()[0][0])
    return Counter(mlist).most_common()[0][0]


if __name__ == '__main__':
    n = int(input())
    find_common(n)
