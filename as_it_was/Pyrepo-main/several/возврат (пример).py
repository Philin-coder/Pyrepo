import shutil  # no
import bs4  # no
import sys  # no
from bs4 import BeautifulSoup  # no
import os  # no
import myconstants  # no
from urllib.request import urlopen  # no
from smtplib import SMTP_SSL  #
from email.mime.multipart import MIMEMultipart  #
from email.mime.base import MIMEBase  #
from email import encoders  #
import lxml.html  #
import time  #

URL = 'https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python '


def func(URL):
    f = myhtml = urlopen(URL)
    sp = BeautifulSoup(myhtml, "html.parser")
    return print(sp)


if __name__ == '__main__':
    func(URL)
