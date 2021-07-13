n = int(input())
m = 0
len_ = len(' '.join(str(i) for i in range(1, n + 1)))
while n > m + 1:
    print(' '.join(str(i) for i in range(n, m, -1)).rjust(len_, ' '))
    m += 1
while m >= 0:
    print(' '.join(str(i) for i in range(n, m, -1)).rjust(len_, ' '))
    m -= 1
