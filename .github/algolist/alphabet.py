import string


def stringer(mstr):
    mstr = string.ascii_letters
    for i in mstr:
        print(i)


if __name__ == '__main__':
    mstr = input()
    stringer(mstr)
