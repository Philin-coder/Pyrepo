comp = 'По результатам собеседования в КОМПАНИЯ были приняты следующие сотрудники'  # утверждение
names = ['Mars', 'Nike', 'Apple', 'Googl']
s = [str.replace(comp, "КОМПАНИЯ", c) for c in names]
print(s)
