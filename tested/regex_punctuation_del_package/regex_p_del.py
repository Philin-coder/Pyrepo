import re


def reg_del_pun(text_str: str) -> str:
    """
    Удаление пунктуации регулярным выражением
    :param text_str: входная текстовая строка(предложенеи с пунктуацией)
    :return:  результирующая строка(предложенеи без пунктуации)
    >>> reg_del_pun(text_str='мир, труд, май')
    мир, труд, май
    'мир труд май'
    >>> reg_del_pun(text_str='МИР, ТРУД, МАЙ')
    МИР, ТРУД, МАЙ
    'МИР ТРУД МАЙ'
    >>> reg_del_pun(text_str='pice, Craft, May')
    pice, Craft, May
    'pice Craft May'
    >>> reg_del_pun(text_str='Миру мир')
    Миру мир
    'Миру мир'

    """
    if isinstance(text_str, str) and len(text_str) > 0:

        print(text_str)
        return re.sub(r'[^\w\s]', '', text_str)
    elif isinstance(text_str, str) and len(text_str) == 0:
        raise ValueError('Введите непустую строку')
    else:
        raise TypeError(f'Введите непустую строку, а не {type(text_str).__name__}')
