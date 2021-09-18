def cezar_crypto(step: int, text_str: str) -> str:
    """
    Реализация шира Цезаря с шагом
    :param step: ключ
    :param text_str: текстовая строка, которую следует зашифроть
    :return:  зашифрованная строка
    >>> cezar_crypto(step=2, text_str='проба')
    'Result: "стргв"'
    >>> cezar_crypto(step=3, text_str='война')
    'Result: "есмрг"'
    >>> cezar_crypto(step=2, text_str='идущие на смерть приветствуют тебя')
    'Result: "кёхыкжбпвбуожтфюбсткджфуфдхафбфжгб"'

    """
    if isinstance(step, int) and isinstance(text_str, str) and step > 0:
        try:
            alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

            letters = [i for i in text_str for i in alpha[(alpha.find(i) + step) % len(alpha)]]
            sp = ''
            return f'Result: "{sp.join(letters)}"'

        except TypeError:
            raise TypeError('Введите ключ(целое, положительное  число) и шифруемую строку маленькими буквами')
    else:
        raise TypeError('Введите ключ(целое, положительное  число) и шифруемую строку маленькими буквами')
