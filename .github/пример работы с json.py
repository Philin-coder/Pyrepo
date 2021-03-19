import json
import random


def listgen(n):
    print(n)
    mlist = [random.randint(1, 10) for i in range(n)]
    j = json.dumps(mlist)
    print(*j)
    return mlist


if __name__ == '__main__':
    assert listgen(n=12)
