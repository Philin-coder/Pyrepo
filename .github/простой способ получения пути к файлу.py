import os


def findpath():
    print(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    findpath()
