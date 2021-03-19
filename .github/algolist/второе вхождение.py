import re


def finder(mstr):
    print(mstr)
    ch = 's'
    index = [i.start() for i in re.finditer(ch, mstr)]
    print(index[1])


if __name__ == '__main__':
    finder(mstr="sims")
