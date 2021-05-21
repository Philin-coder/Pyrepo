m1 = int(input())
m2 = int(input())
if m2 > m1:
    m1, m2 = m2, m1
while(True):
    a = int(input())
    if a == 0:
        break
    if a > m1:
        m1, m2 = a, m1
    elif a > m2:
        m2 = a
print(m2)
