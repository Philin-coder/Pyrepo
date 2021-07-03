r = conn.execute(s)
row = r.fetchone()
print(row)
print(type(row))
print(row['id'], row['first_name'])  # доступ к данным по названию колонки
print(row[0], row[1])  # доступ к данным по индексу
print(row[customers.c.id], row[customers.c.first_name])  # доступ к данным через объект класса
print(row.id, row.first_name)  # доступ к данным, как к атрибуту

