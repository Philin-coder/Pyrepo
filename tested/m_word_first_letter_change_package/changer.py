def changer_word_first_letters_func(text_str: str) -> str:
    """
    Замена слов на первые буквв данных слов
    :param text_str: текстовая строка
    :return: строка, в которой слова заменены первыми буквами этих же слов
    >>> changer_word_first_letters_func(text_str='Мама мыла раиу')
    'Ммр'
    >>> changer_word_first_letters_func(text_str='Peace abd love')
    'Pal'
    """

    if isinstance(text_str, str) and not any(i.isdigit() for i in text_str) and len(text_str) > 0:
        return ''.join([i[0] for i in text_str.split()])
    else:
        raise TypeError('Введите  непустую  строку')
