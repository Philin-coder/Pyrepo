import os


def disk_letter_func(letters: tuple) -> list:
    """
    Определение установленных логических дисков.
    :param letters: список возможных (буквенных)имен дисков.
    :return: список установленных hdd.
    >>> disk_letter_func(letters=(
    ... 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    ... 'W', 'X', 'Y', 'Z'))
    ['C:', 'D:', 'E:', 'F:', 'G:']

    """
    if isinstance(letters, tuple) and letters is not None:
        drives = ['{0}:'.format(d)
                  for d in letters if os.path.exists('{0}:'.format(d))]
        return drives
    else:
        raise TypeError('Передан неверный тип данных')
