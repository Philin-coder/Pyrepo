class SeaMap(object):
    def __init__(self):
        self.m = []
        for row in range(10**4):
            r = []
            for col in range(10**4):
                r.append('.')
            self.m.append(r)
 
    def shoot(self, x, y, s):
        if s == 'miss':
            f = '*'
        # ...
        self.m[x][y] = f
 
    def cell(self, x, y):
        return self.m[x][y]
 
 
sm = SeaMap()
sm.shoot(2, 0, 'miss')
sm.shoot(6, 9, 'miss')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()