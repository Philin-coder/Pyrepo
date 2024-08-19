from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_html(url):
    my_html = urlopen(url)
    return BeautifulSoup(my_html, "html.parser")


if __name__ == '__main__':
    print(get_html(url='http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/'))
