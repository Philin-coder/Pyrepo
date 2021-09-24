def set_enq_func(text_str: str, text_str2: str) -> [bool, str]:
    """
    Иллюстрация работы с множествами
    :param text_str:входная строка
    :param text_str2: вторая входная строка
    :return:  результат проверки на равенство множеств, или, подмножество

    """
    if isinstance(text_str, str) and isinstance(text_str2, str):
        print(set(text_str))
        print(set(text_str2))
        if set(text_str) == set(text_str2):
            return 'множества равны'
        else:
            if set(text_str) != set(text_str2):
                return 'множества  не равны'
    else:
        raise TypeError('введите 2 строки')


def subset_test_func(text_str, text_str2: str) -> bool:
    if isinstance(text_str, str) and isinstance(text_str2, str):
        return set(text_str).issubset(text_str2)
    else:
        raise TypeError('Введите 2 строки')
