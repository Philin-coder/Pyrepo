class rect:
    def __init__(self, dl, sh):
        self.dl = dl
        self.sh = sh

    def printer(self):
        print(self.dl)
        print(self.sh)

    def area(self):
        print(self.dl * self.sh)


class square(rect):

    def __init__(self, size):
        super().__init__(size, size)


if __name__ == '__main__':
    sq = square(2)
    sq.printer()
    sq.area()