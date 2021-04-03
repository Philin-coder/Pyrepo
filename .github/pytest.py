
# 3.3) В строках оставить только латинские буквы и пробелы. Прочие символы удалить.
# 3.4) Объединить список в единую строку. вывести на печать.
# 3.5) Подсчитать количество вхождений различных слов в тексте. Подсчет вести в словаре.
# 3.6) Вывести на печать 10 наиболее популярных и наименее популярных слов (“ 1) -- hello -- 15”).
# 3.7) Заменить наименее популярные слова на “PYTHON”.
# 3.8) Создать новый txt-файл.
# 3.9) Записать текст в файл, разбивая на строки, при этом на
import wikipedia


def test(my_filename, fext2):
    wikipedia.set_lang("en")
    res = wikipedia.summary('hindy')
    with open(my_filename+'.'+fext2, 'w', encoding='utf-8') as fp:
        print(res, file=fp, sep="\n")


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
    print(data)
    str_list=list(filter(None,data))
    for i in str_list:
        print(i)
    #print(str_list)



    



if __name__ == '__main__':
    my_filename = None
    fext2 = None
    test(my_filename='test', fext2='txt')
    reader(my_filename='test', fext2='txt')
