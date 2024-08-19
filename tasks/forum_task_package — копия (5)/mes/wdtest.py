import os
import glob
import selenium
from selenium import webdriver

drv = webdriver.Chrome()
drv.get('https://web.whatsapp.com/')
while True:
    aim = glob.glob('*.exe')
    path = os.getcwd() + '\\' + 'chromedriver.exe'
# print(aim)
