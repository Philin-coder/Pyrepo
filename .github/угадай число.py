import random

NumberToGuess = random.randint(1, 100)
userGuess = -1
while userGuess != NumberToGuess:
    userGuess = int(input("Угадай число от 1 до 100"))
    if userGuess > NumberToGuess:
        print("Число должно быть меньше!")
    elif userGuess < NumberToGuess:
        print("Число должно быть больше!")
    else:
        print("Вы угадали, это число = " + str(NumberToGuess))
    break
