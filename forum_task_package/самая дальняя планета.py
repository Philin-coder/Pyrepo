orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1]))