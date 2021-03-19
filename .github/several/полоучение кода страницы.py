import requests
import pygame
import os
import sys
import binascii
from pygame.locals import *
import shutil
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import lxml.html
import sqlite3
import urllib

url = 'http://htmlbook.ru/samhtml5/ustarevshie-tegi-i-atributy/'


def get_html(url):
    f = myhtml = urlopen(url)
    # print(f)
    sp = BeautifulSoup(myhtml, "html.parser")
    print(sp)


if __name__ == '__main__':
    get_html(url)
