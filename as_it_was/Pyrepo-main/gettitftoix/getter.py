import requests
import pygame
import os
import sys

# import binascii
# import myconstants
# from myconstants import *
# from pygame.locals import *
# import shutil
# import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


# from smtplib import SMTP_SSL
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# import lxml.html
# import sqlite3


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
        print(linklist, file=fp, sep="\n")

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


def folderer(nput, nname):
    os.mkdir(nname)
    os.chdir(os.getcwd() + '\\' + nname + '\\')
    print(os.getcwd())


def myf(myhttp):
    ms = str(input("введите название сохраняемого трека" + ' '))
    req = requests.get(myhttp, stream=True)
    if req.status_code == status:
        with  open(ms + '.' + fext, 'wb') as fp:
            fp.write(req.content)
    put = (os.getcwd())
    files = []
    for i in os.listdir(put):
        if i.endswith(fext):
            files.append(i)
    for i in files:
        print(i)


def mplayer(playlist):
    for i in os.listdir(os.getcwd()):
        if i.endswith(fext):
            playlist.append(i)
        print('список песен равен')
        print(playlist)
        for i in range(len(playlist)):
            pygame.init()
            wnd = pygame.display.set_mode((640, 640))
            pygame.mixer.music.load(playlist[i])
            pygame.mixer.music.play(-1, 0.0)
            circule = pygame.draw.circle(wnd, (50, 30, 90), (90, 30), 16, 5)
            wnd.blit(wnd, circule)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()


if __name__ == '__main__':
    playlist = []
    fname = str(input("название папки" + ' '))
    my_filename = str(input("введите имя файла" + ' '))
    whattoread = my_filename
    linklist = []
    nname = str(input("названеи папки" + ' '))
    nput = os.getcwd()
    s = int(input("сколько раз вывести"))
    Mparser(URL, my_filename)
    reader(whattoread)
    folderer(nput, nname)
    for i in range(s):
        myf(myhttp)
    mplayer(playlist)
