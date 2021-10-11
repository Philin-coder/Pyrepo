# TODO:Two
from win32com.client import Dispatch
from sys import platform
import os

print(platform.lower())
midsk = []
fso = Dispatch('Scripting.FileSystemObject')
for drive in fso.Drives:
    drive = str(drive)
    midsk.append(drive)
print(midsk)
