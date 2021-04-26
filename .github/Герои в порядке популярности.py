d={}
while True:
    data = input()
    if data =="конец":
        break
    name, comment = data.split()
    d.setdefault(name, set()).add(comment)
for name in d:
    print(f'Количество уникальных комментаторов у {name} - {len(d[name])}')