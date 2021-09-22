def drawMatrix(matrix):
    # Матрица в формате [[], [], []]
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()


def matrixHorizontalReflection(matrix):
    # Матрица в формате [[], [], []]
    # Есть идея выводить каждую матрицу в обратной порядке с помощью функции reversed()
    for i in matrix:
        for j in reversed(i):
            print(j, end=' ')
        print()


def matrixVerticalReflection(matrix):
    # Здесь можно выводить в отдельный список столбей и строчку из списка,
    # переворачивать, и вставлять обратно
    for i in reversed(matrix):
        for j in i:
            print(j, end=' ')
        print()


def matrixTranpone(matrix):
    for i in list(zip(*matrix)):
        for j in i:
            print(j, end=' ')
        print()
