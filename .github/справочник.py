def searh():
    name = input('> ')
    if name in phone_book:
        return f'{name} {phone_book[name]}'
    else:
        return 'Error'


with open('test.txt') as file:
    data = file.read().splitlines()

phone_book = {}
for line in data:
    name = list(filter(lambda x: x.isalpha() or x == ' ', line))
    number = line[len(name):]
    name = ''.join(name).strip()
    phone_book[name] = number
    print(line)

print(searh())
