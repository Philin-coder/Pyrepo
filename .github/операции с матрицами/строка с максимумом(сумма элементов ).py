matrix = [
    [1, 2, 3],
    [9, 8, 7],
    [4, 5, 6]
]

index, maximum = 0, 0
for i, _maximum in enumerate(map(max, matrix)):
    if maximum < _maximum:
        index, maximum = i, _maximum

print(sum(matrix[index]))
