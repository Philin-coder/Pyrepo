# TODO: and me
# игра по угадыванию числа
import random

guessesTaken = 0

print('Привет! Как тебя зовут?')

myName = input()

number = random.randint(1, 20)
print('Что же, ' + myName + ', я загадаю чило от 1 до 20.')

for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = int(input())
    guess = int(guess)

    if guess < number:
        print('Твое чило слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Отлино, ' + myName + 'Ты справился за ' + guessesTaken + 'попытки!')

    if guess != number:
        pass
# number = '<'
# not supported
# between
# instances
# of
# 'int' and 'str'(number)
# print('Увы. Я загадал число ' + number + '.')
