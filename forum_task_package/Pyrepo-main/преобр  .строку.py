import collections  # импорт коллекций(библиотека)

input_string = 'aaabbbcc'  # входная строка
output_string = '@'  # выходная

d = collections.defaultdict(int)  # ckdjfhm колллекций(по умолчанию, который, конвертируем в число ключ)
for c in input_string:  # ищем значение в строке, получаемой программой
    d[c] += 1  # наращиваем, коль нашли,

for c in sorted(d, key=d.get, reverse=True):  # выводим в обратнном порядке
    output_string = output_string + '%d%s' % (
        d[c], c)  # в тех местах, где стояли считаемые значения, вставляем их колмчество

print(output_string)  # вывд
