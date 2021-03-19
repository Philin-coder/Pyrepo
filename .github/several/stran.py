from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen


def getTitle(url):
    try:
        html = urlopen(url)

    except HTTPError as e:

        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://fishki.net/1319528-evrejskie-anekdoty.html")
if title == None:
    print("title not found")
else:
    print(title)
