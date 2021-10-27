import os
from os import listdir


def folder_explorer() -> str:
    return '\n'.join(listdir(os.getcwd()))


if __name__ == '__main__':
    print(folder_explorer())
