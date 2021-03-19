c = 'аиеёэоуыэяюАЁИЮЭЫУЕОЯ.,!?-;:'
a = 'Удивительный факт, но '
b = ''.join([i for i in a if i not in c])
print(b)
