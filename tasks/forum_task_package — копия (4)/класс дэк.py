class Deque(object):
    def __init__(self):
        self.dllist = []

    def is_empty(self):
        return self.dllist == []

    def addfront(self, item):
        self.dllist.append(item)

    def addrear(self, item):
        self.dllist.insert(0, item)

    def removefront(self):
        return self.dllist.pop()

    def removerear(self):
        return self.dllist.pop(0)

    def size(self):
        return len(self.dllist)


if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    print(d.addrear(4))
    print(d.addrear('dog'))
    print(d.addrear('cat'))
    print(d.addfront(True))
    print(d.size())
    print(d.is_empty())
    print(d.addrear(8.4))
    print(d.removerear())
    print(d.removefront())