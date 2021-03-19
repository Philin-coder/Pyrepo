# Пример генерации списка
list_1 = range(1, 101)
list_comp = [val for val in list_1 if val % 2 == 0]
print(list_comp)
