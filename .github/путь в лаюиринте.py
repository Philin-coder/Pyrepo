m = [
    [0, -1, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, -1, 0],
    [-1, -1, -1, -1, 0],
    [0, 0, -1, 0, 0],
]


def show(m):
    for i in m:
        for j in i:
            print('{: 3}'.format(j), end='')
        print()
    print('----')


points = [(0, 0)]
step = 1
while True:
    show(m)
    points_new = []
    for x, y in points:
        m[x][y] = step
        # u
        if x - 1 >= 0 and m[x - 1][y] == 0:
            points_new.append((x - 1, y))
        # d
        if x + 1 < 5 and m[x + 1][y] == 0:
            points_new.append((x + 1, y))
        # r
        if y + 1 < 5 and m[x][y + 1] == 0:
            points_new.append((x, y + 1))
        # l
        pass
    points = points_new
    step += 1
    if m[-1][-1] != 0:
        print('ok')
        break
    print(points)
    if not points:
        print('fail')
        break
show(m)
print(m[-1][-1] - 1)
