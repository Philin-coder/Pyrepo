import shutil  # no
import bs4  # no
import sys  # no
from bs4 import BeautifulSoup  # no
import os  # no
import myconstants  # no
from myconstants import  # no
from urllib.request import urlopen  # no
from smtplib import SMTP_SSL  #
from email.mime.multipart import MIMEMultipart  #
from email.mime.base import MIMEBase  #
from email import encoders  #
import lxml.html  #
import time  #


def Mparser(URL, my_filename):
    f = myhtml = urlopen(URL)
    sp = BeautifulSoup(myhtml, "html.parser")
    lnk = sp.findAll("a", class_="playlist-btn-down")
    os.mkdir(fname)
    os.chdir(os.getcwd() + '\\' + fname + '\\')
    char = "'"
    for l in lnk:
        l = str(l)
        l = l.replace('"', ' ')
        l = l.replace('<a class=', ' ')
        l = l.replace('playlist-btn-down no-ajaxy', '')
        l = l.replace('\'', '')
        l = l.replace('target= _blank  title= скачать >(скачать)</a>', ' ')
        l = l.replace('download', 'listen')
        l = l.replace('href=', ' ')
        linklist.append(l)
        print(linklist)
    with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
        print(*linklist, file=fp, sep="\n")
        fp.close()
    return linklist


def reader(whattoread):
    with open(whattoread + '.' + fext2, 'r', encoding='utf-8') as fp1:
        playlist = []
        str = ''
        playlist = fp1.readlines()
        fp1.close()
        print('список песен')
        for c in range(len(playlist)):
            time.sleep(2)
            str = str.replace(str, playlist[c])
            print(str)


if __name__ == '__main__':
    fname = str(input("название папки" + ' '))
    my_filename = str(input("введите имя файла" + ' '))
    whattoread = my_filename
    linklist = []
    Mparser(URL, my_filename)
    reader(whattoread)
