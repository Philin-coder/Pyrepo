import re
import string


def ner(text):
    ame = 'АОИЕЁЭЫУЮЯаоиеёэыуюя' + string.punctuation

    text = re.sub(r'[{}]'.format(ame), '', text)
    text = ' '.join(map(str.strip, text.split()))
    print(text)


if __name__ == '__main__':
    text = "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать."
    ner(text)
