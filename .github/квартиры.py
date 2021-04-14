x, y = map(int, input().split())
a = y - x + 1  # Находим длину этажа
if (x - 1) % a == y % a == 0:  # Проверяем являются ли данные этажи первым и последним
    print('YES')
else:
    print('NO')
