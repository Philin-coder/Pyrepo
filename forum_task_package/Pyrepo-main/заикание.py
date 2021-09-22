text = """\
Привет
Не могу до тебя дозвониться
Не могу до тебя дозвониться
Не могу до тебя дозвониться
Когда доедешь до дома
Ага, жду
Ага, жду"""

splt = text.split('\n')

if len(splt) >= 1:
    tmp = splt[0]
    print(tmp)
    for line in splt[1:]:
        if line != tmp:
            tmp = line
            print(tmp)