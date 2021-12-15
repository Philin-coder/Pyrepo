def speach_defect(text: str) -> list[str]:
    """
    Заикание
    помогите исправить код, не знаю что не так. Условие:
    Из-за плохой связи на мобильный телефон Василия приходят одни и те же смски по несколько раз. Он попросил вас написат
    ь небольшую функцию, которая будет работать почти как обычный print, но не будет печатать сообщение, если предыдущее
    сообщение было таким же.
    Чтобы телефон эти изменения в распечатке смсок принял, ваш друг настроил его так, что вам достаточно написать функци
    ю print_without_duplicates(message). Напишите её.
    :param text: входной текст
    :return:результирующий текст
    """
    if isinstance(text, str) and text != '' and text is not None:
        sp = text.split('\n')
        words = list()
        if len(sp) >= 1:
            tmp = sp[0]
            print(tmp)
            for line in sp[1:]:
                if line != tmp:
                    tmp = line
                    print(tmp)
                    words.append(tmp)
            return words
    else:
        raise TypeError('Передан неверный тип данных')
