from collections import Counter


def solution():
    word = input()
    letters = Counter(word)
    result = [[]]
    for letter in word:
        letters[letter] -= 1
        result[-1].append(letter)
        if all(letters[c] == 0 for c in result[-1]):
            result.append([])
    print(*map("".join, result))


if __name__ == "__main__":
    solution()
