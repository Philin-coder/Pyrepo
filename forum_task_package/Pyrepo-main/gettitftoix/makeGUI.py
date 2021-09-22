import os
import sys
import re


def filer(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        tegs = []
        res = []
        tegs = fp.readlines()
        fp.close()

        tegs = str(tegs)
        print(tegs)
        fstr = ''
        fstr = str(input("введите строку"))
        for i in re.findall(fstr, tegs):
            # print(i)
            res.append(i)
        print(res)


if __name__ == '__main__':
    filename = '1.txt'
    filer(filename)
