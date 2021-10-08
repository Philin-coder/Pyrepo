import random


def create_matrix():
    n = int(input("строка  и столбцы: "))
    matr = [[random.randint(0, 9) for i in range(n)] for j in range(n)]
    return matr


def show_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


my_matrix = create_matrix()
show_matrix(my_matrix)
