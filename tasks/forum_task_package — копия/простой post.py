import sys
import urllib.request
import time
import urllib.parse


def poster(myhtml, data):
    data.encode("ascii")
    print(sys.version_info)
    response = urllib.request.urlopen(myhtml, data)
    hmtl = response.read().decode("utf-8")
    print(hmtl)
    time.sleep(10)


if __name__ == '__main__':
    poster(myhtml="http://www.yandex.ru", data="z=555")
