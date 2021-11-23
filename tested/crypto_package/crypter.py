import random


def crypto(string_to_crypt: str, key: int) -> str:
    """
    Шифрование методом перестановки.
    :param string_to_crypt: шифруемая строка
    :param key: ключ шифрования.
    :return:  Зашифрованная строка
    >>> crypto(string_to_crypt='Скажи мне, кто твой друг и я скажу тебе, кто ты', key=5)
    ',вукукстж нгкы мйеСтаое тяаи  о ите дбтрож  , к'
    """
    if isinstance(string_to_crypt, str) and all(
            [isinstance(i, str) for i in string_to_crypt]) and not any(
        [i.isdigit() for i in string_to_crypt]) and string_to_crypt != '' and isinstance(key, int) and key is not None:
        random.seed(key)
        keys = random.sample(range(len(string_to_crypt)), len(string_to_crypt))
        out = ''
        for i in keys:
            out += string_to_crypt[i]
        return out
    else:
        raise TypeError('Передан неверный тип данных')


def encrypt(string_to_encrypt: str, key: int) -> str:
    """
    Расшифровка методом перестановки.
    :param string_to_encrypt: дешифруемая строка.
    :param key: ключ
    :return: расшифровка строки
    >>> encrypt(string_to_encrypt=crypto(string_to_crypt='Скажи мне, кто твой друг и я скажу тебе, кто ты', key=5),
    ...                   key=5)
    'Скажи мне, кто твой друг и я скажу тебе, кто ты'
    """
    if isinstance(string_to_encrypt, str) and all(
            [isinstance(i, str) for i in string_to_encrypt]) and string_to_encrypt is not None and isinstance(key, int) \
            and key is not None:
        random.seed(key)
        keys = random.sample(range(len(string_to_encrypt)), len(string_to_encrypt))
        out = [' ' for _ in range(len(string_to_encrypt))]
        for i, j in zip(keys, string_to_encrypt):
            out[i] = j
        return ''.join(out)
    else:
        raise TypeError('Передан неверный тип данных')
