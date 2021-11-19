import bs4
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen
import requests
from requests.exceptions import HTTPError


def get_page(url: str) -> bs4.element.Tag:
    """
    Получение определенных тегов web - страницы
    :param url: web-адрес.
    :return: часть объекта BS.
    Образец вызова
    get_page(url='https://fishki.net/1319528-evrejskie-anekdoty.html')
    """
    if isinstance(url, str) and url != '':
        try:
            code = requests.get(url)
            code.raise_for_status()
            my_html = urlopen(url)
            bs = BeautifulSoup(my_html.read(), "html.parser")
            return bs.body.h1
        except HTTPError as http_err:
            raise f'HTTP error occurred: {http_err}'
        except Exception as err:
            raise f'Other error occurred: {err}'

    else:
        raise TypeError('Передан неверный тип данных, или -пустая строка')
