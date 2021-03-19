def func(a: int, b: int) -> list:
    return list(range(a, b + 1))


assert func(1, 5) == [1, 2, 3, 4, 5]

A = int(input())
B = int(input())
print(*func(A, B))
