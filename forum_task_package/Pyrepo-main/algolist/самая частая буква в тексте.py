import string


def out_chr(text):
    print(max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch)))
    return max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))


if __name__ == '__main__':
    text = input()
    out_chr(text)
