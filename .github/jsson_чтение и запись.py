import json


def j_writer(n):
    mdict = dict(input().split() for _ in range(n))
    with open("data.json", 'w') as fp:
        json.dump(mdict, fp)
    with open("data.json", 'r')as fp:
        res = json.load(fp)
    print(res)


if __name__ == '__main__':
    n = int(input())
    j_writer(n)

