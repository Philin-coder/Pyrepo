import os


def find_path() -> str:
    """
    :return: путь к файлу в папке


    """
    return os.path.dirname(os.path.abspath(__file__))

