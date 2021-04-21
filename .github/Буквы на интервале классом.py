class Letter:
    def __init__(self, letter: str):
        self.value = letter.lower()
        self.upper = letter.upper()

    def __str__(self):
        return f'{self.upper}{self.value}'


def letters_range(first_letter, second_letter) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    min_, max_ = sorted([letters.index(first_letter),
                        letters.index(second_letter)])
    return ' '.join(str(Letter(letters[index])) for index in range(min_, max_ + 1))


if __name__ == '__main__':
    assert letters_range('a', 'd') == 'Aa Bb Cc Dd'
    assert letters_range('e', 'a') == 'Aa Bb Cc Dd Ee'
