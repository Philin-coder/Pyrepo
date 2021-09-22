import os

names = os.listdir(os.getcwd())
for name in names:
    fullname = os.path.join(os.getcwd(), name)
    if os.path.isfile(fullname):
        print(fullname)
