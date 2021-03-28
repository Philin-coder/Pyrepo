#!/usr/bin/env python3
 
class SeaMap(object):
    def __init__(self):
        self.field = [ list('.')*10 for _ in range(10) ]
 
    def shoot(self, row, col, result):
        self.field[row][col] = {
            'miss': '*',
            'hit': 'x',
            'sink': 'x',
        }[result]
 
    def cell(self, row, col):
        f = self.field[row][col]
        if f == 'x':
            return 'x'
        elif f == '*':
            return '*'
        elif f == '.':
            return '*' if self._f(row, col) else '.'
 
    def _f(self, x, y):
        f1 = self._g(x-1, y-1)
        f2 = self._g(x-1, y)
        f3 = self._g(x-1, y+1)
        f4 = self._g(x, y-1)
        f5 = self._g(x, y+1)
        f6 = self._g(x+1, y-1)
        f7 = self._g(x+1, y)
        f8 = self._g(x+1, y+1)
        return 'x' in (f1, f2, f3, f4, f5, f6, f7, f8)
 
    def _g(self, x, y):
        try:
            return self.field[x][y]
        except IndexError:
            return '.'
 
 
 
sm = SeaMap()
 
sm.shoot(0, 0, 'hit')
sm.shoot(0, 1, 'sink')
 
sm.shoot(9, 8, 'hit')
sm.shoot(9, 9, 'sink')
 
sm.shoot(2, 3, 'sink')
 
sm.shoot(5, 6, 'miss')
sm.shoot(7, 8, 'miss')
sm.shoot(1, 7, 'miss')
 
sm.shoot(1, 7, 'miss')
 
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()