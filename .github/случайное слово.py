# -*- coding: utf-8 -*-
import random
 
words = {"hello": "привет", "world": "мир"}
 
errors = 0
while errors < 10:
    eng, rus = list(words.items())[random.randint(0, len(words)-1)]
    if input("%s = " % eng).lower() == rus:
        print("Верно")
    else:
        print("Не верно.")
        errors += 1