import re

with  open("2.txt", encoding="utf-16") as fd:
    text2 = fd.read()

with open("1.txt") as fd:
    for pattern in fd:
        pattern = pattern.strip()
        if pattern:
            regex = "^(.+{}.+)$".format(re.escape(pattern))
            text2 = re.sub(regex, '', text2, flags=re.MULTILINE)
# удаление пустых строк
text2 = re.sub(r'\n\s*\n', '\n', text2, re.MULTILINE)
# новый файл - можете указать имя прежнего файла
with open("2new.txt", "w", encoding="utf-16") as f:
    f.write(text2)
