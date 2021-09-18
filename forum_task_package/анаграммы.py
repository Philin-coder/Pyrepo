# Функция проверяет являются ли слова
# word1 и word2 анаграммами
def test(word1, word2):
    a1 = list(word1)
    a2 = list(word2)
    if set(a1) == set(a2):
        return True
    else:
        return False


# Ввод n
n = int(input())

# Ввод слов
words = []
for _ in range(n):
    word = input().lower()
    if not word in words:
        words.append(word)

# Сортировка слов как в словаре
words = sorted(words, key=lambda w: w)

while len(words) > 0:
    w = [words.pop(0)]

    k = 0
    while k < len(words):
        word2 = words[k]

        if test(w[0], word2):
            w.append(word2)
            words.remove(word2)
        else:
            k += 1

    if len(w) > 1: print(*w)
