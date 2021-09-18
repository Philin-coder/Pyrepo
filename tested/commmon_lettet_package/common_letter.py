import string


def most_common_english_letter(text_str: str) -> str:
    """
    поиск самой частой английской буквы вв строке
    :param text_str:
    :return: самая часто встречаемая буква
    >>> most_common_english_letter(text_str='test list fast')
    test list fast
    't'
    >>> most_common_english_letter(text_str='fast test of list')
    fast test of list
    't'
    >>> most_common_english_letter(text_str='for honour')
    for honour
    'o'

    """
    letters_upper = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W',
        'X', 'Y', 'Z')
    letters_lower = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w',
        'x', 'y', 'z')
    if isinstance(text_str, int):
        raise TypeError('не вводить цифры')
    else:
        if isinstance(text_str, str) and len(text_str) > 0 and text_str != '' and any(
                i in text_str for i in letters_upper) or any(i in text_str for i in letters_lower):
            print(text_str)
            return max(string.ascii_lowercase, key=lambda ch: text_str.lower().count(ch))
        else:
            raise TypeError('Введите строку на английском ')
