import subprocess


def shell_commander(text_str: str) -> str:
    """
    Работа с командами и subprocess.
    :param text_str: команда
    :return: код состояния
    Образец вызова
    shell_commander(text_str='ping ya.ru')

    Обмен пакетами с ya.ru [87.250.250.242] с 32 байтами данных:
    Ответ от 87.250.250.242: число байт=32 время=28мс TTL=246
    Ответ от 87.250.250.242: число байт=32 время=28мс TTL=246
    Ответ от 87.250.250.242: число байт=32 время=28мс TTL=246
    Ответ от 87.250.250.242: число байт=32 время=28мс TTL=246

    Статистика Ping для 87.250.250.242:
        Пакетов: отправлено = 4, получено = 4, потеряно = 0
        (0% потерь)
    Приблизительное время приема-передачи в мс:
        Минимальное = 28мсек, Максимальное = 28 мсек, Среднее = 28 мсек
    0
    'command done'

    """
    if isinstance(text_str, str):
        text_str.encode('Utf-8').decode('windows-1251')
        print(subprocess.call(text_str, shell=True))
        stat_code = 'command done'
        return stat_code

    else:
        raise TypeError('Передан неверный тип данных')
