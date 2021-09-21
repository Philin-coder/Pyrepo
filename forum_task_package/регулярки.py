import re


def reader(my_filename, fext2):
    with open(my_filename + '.' + fext2, 'r', encoding='utf-8') as fp:
        data = fp.readlines()
        data = str(data)
        res = re.findall(r'.', data)
        # res=re.findall(r'\w',data)
        # res=re.findall(r'\w*',data)
        # res=re.findall(r'\w+',data)
        # res=re.findall(r'^\w+','AV is largest Analytics community of India')
        # res=re.findall(r'\w+$' ,'AV is largest Analytics community of India')
        # res=re.findall(r'\w\w',data)
        # res=re.findall(r'\b\w\w.',data)
        # res=re.findall(r'@\w+.(\w+)',data)

        print(res)


if __name__ == '__main__':
    my_filename = None
    fex2 = None
    reader(my_filename='проба', fext2='txt')
