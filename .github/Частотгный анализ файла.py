from collections import Counter


def chast():
    with open("letters.txt", 'r') as fp:
        c = Counter()
        for x in fp:
            c += Counter(x.strip())
    print(c)


if __name__ == '__main__':
    chast()
