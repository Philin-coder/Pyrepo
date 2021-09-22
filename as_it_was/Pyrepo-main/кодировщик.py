import urllib.request


def reader(html, mfilename):
    page = urllib.request.urlopen(html)
    # print(page.read())
    mlist.append(page.read())

    with open(mfilename + '.' + 'txt', 'w', encoding='utf-8') as fp:
        print(mlist, file=fp)


def rsorting(mfilename, mlist2, mlist3):
    with open(mfilename + '.' + 'txt', 'r', encoding='utf-8') as fp:
        for i in fp:
            print(i)


if __name__ == '__main__':
    mfilename = 'проба'

    html = 'https://www.rupython.com/html-212.html'
    mlist = []
    mlist2 = []
    mlist3 = []
    reader(html, mfilename)
    rsorting(mfilename, mlist2, mlist3)
