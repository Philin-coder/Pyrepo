n = int(input())
k = int(input())
print(max(n - 3 - (k - 1), 0) if k < n // 2 + 1 else max(n - 3 - (n - k), 0))
