from bs4 import BeautifulSoup
from urllib.request import urlopen
from requests.exceptions import HTTPError
import re


def get_html(url: str) -> [str, set]:
    """
    Пролучение списка тегов на web-странице.
    :param url: web-адрес
    :return: списоок уникальных теговою.
    Образец вызова
    get_html(url='http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/')
    """
    if isinstance(url, str) and url != '':
        try:
            my_html = urlopen(url)
            sp = BeautifulSoup(my_html, "html.parser")
            lnk = sp.find_all("span", class_="tag")
            return set(re.findall(r'\b[^\b<span cl="tg>&;]\w+', str(lnk)))
        except HTTPError as http_err:
            raise f'HTTP error occurred: {http_err}'
        except Exception as err:
            raise f'Other error occurred: {err}'
    else:
        raise TypeError('Передан неправильный тип данных, либо - пустая строка')
