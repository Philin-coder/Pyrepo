class Myrectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def crossing(self, f):
        if ((f.x > self.x + self.w) or (f.y > self.y + self.h) or
                (self.x > f.x + f.w) or (self.y > f.y + f.h)):
            print('None')
            return None
        else:
            P1 = set()
            for y in range(self.y, self.y + self.h + 1):
                for x in range(self.x, self.x + self.w + 1):
                    P1.add((x, y))
            P2 = set()
            for y in range(f.y, f.y + f.h + 1):
                for x in range(f.x, f.x + f.w + 1):
                    P2.add((x, y))
            P3 = P1 & P2
            print(P3)
            return P3


if __name__ == '__main__':
    rect1 = Myrectangle(0, 0, 10, 10)
    rect2 = Myrectangle(5, 5, 10, 10)
    rect3 = rect1.crossing(rect2)
