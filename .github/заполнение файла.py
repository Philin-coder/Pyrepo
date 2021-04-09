
import wikipedia



def wiki(mstr, n, my_filename, fext2):
    wikipedia.set_lang('ru')
    res = wikipedia.summary(mstr, sentences=n)
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(res, file=fp, sep="\n")


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
        print(data)


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    wiki(mstr='Россия', n=150, my_filename='test', fext2='txt')
    reader(my_filename='test', fext2='txt')
