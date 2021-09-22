def listcounter():
    mlist = ['Bob', 'Alice', 'Jane', 'Bob', 'Alice']
    print(*mlist)
    print(dict((i, mlist.count(i)) for i in set(mlist) if mlist.count(i) > 1))
    return mlist


if __name__ == '__main__':
    assert listcounter()


