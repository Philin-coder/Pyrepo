stroka = input().split()
h = int(stroka[0])
m = int(stroka[1])
s = int(stroka[2])
h = h // 30
m = m // 6
if s % 6 != 0:
    for i in range(2):
        s += 1
        if s % 6 == 0 and s / 6 != 60:
            s = s / 6
            break
        elif s / 6 == 60:
            s = 0
            break
    if s % 6 != 0:
        s -= 2
        for i in range(2):
            s -= 1
            if s % 6 == 0:
                s = s / 6
                break
else:
    s = s / 6
if m == 60:
    m = 0
if h < 10:
    h = '0' + str(h)
if m < 10:
    m = '0' + str(m)
time = str(h) + ':' + str(m) + ':' + '0' + str(int(s))
print(time)
