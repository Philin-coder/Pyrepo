f = open('tekstovi.txt', 'w', encoding='utf-8')
f.write('yes')
f.close()
f = open('tekstovi.txt')
end = f.read()
while end is not None:
    f.read()
    print(f)
