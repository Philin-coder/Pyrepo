import urllib3
from urllib.request import urlopen
import requests
from urllib.parse import urljoin
from lxml.html import fromstring


def Mparse():
    import urllib.request
    with urllib.request.urlopen("https://www.investing.com/equities/") as url:
        s = url.read()
    # I'm guessing this would output the html source code?
    print(s)


if __name__ == '__main__':
    Mparse()
