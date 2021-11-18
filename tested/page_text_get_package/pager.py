import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from requests.exceptions import HTTPError


def page_get_func(url: str) -> bs4.BeautifulSoup:
    """
    Работа с библиотекой bs4(получение текста web-страницы)
    :param url: строка(web-адрес )
    :return: текст web-страница
    Образец вызова
    page_get_func(
            url='https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python '))
    """
    if isinstance(url, str) and url != '':
        try:
            code = requests.get(url)
            code.raise_for_status()
            my_html = urlopen(url)
            return BeautifulSoup(my_html, "html.parser")
        except HTTPError as http_err:
            raise f'HTTP error occurred: {http_err}'
        except Exception as err:
            raise f'Other error occurred: {err}'

    else:
        raise TypeError('Передан неверный тип данных, или -пустая строка')
