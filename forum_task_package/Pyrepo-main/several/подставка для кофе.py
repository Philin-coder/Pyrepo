import sys, os, pygame, time
import pygame.cdrom as cdrom

while 1:
    cdrom.init()
    cd = cdrom.CD(0)
    cd.init()
    cd.eject()
    cd.quit()
    cdrom.quit()
time.sleep(5)
