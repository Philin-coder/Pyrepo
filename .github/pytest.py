# Из слова «программа» путем "вырезок" и "склеек" его букв получить слова
# «рог», «рама», «рампа», «пора», «гамма», «грамм».
mstr = 'программа'
print(mstr)
print(mstr[1:4])  # рог
print(mstr[4:7]+mstr[8])  # рама
print(mstr[4:7]+mstr[0]+mstr[8])  # рампа
print(mstr[0]+mstr[2]+mstr[1]+mstr[8])  # пор а
print(mstr[3]+mstr[8]+mstr[6]*2+mstr[8])  # гамма
print(mstr[3]+mstr[4]+mstr[8]+mstr[6]*2)
