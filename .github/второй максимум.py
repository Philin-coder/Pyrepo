m1 = int(input())
m2 = None
while True:
    a = int(input())
    if a == 0:
        print(m2)
        break
    elif a > m1:
        m1, m2 = a, m1
    elif m2 == None:
        m2 = a
    elif a > m2:
        m2 = a
