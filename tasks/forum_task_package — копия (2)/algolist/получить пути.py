import os
import inspect


def get_script_dir():
    return os.path.dirname(inspect.getabsfile(get_script_dir))


# путь до родительского каталога скрипта
app_dir = get_script_dir()  # способ для "замороженных" скриптов Cx_Freeze
app_dir = os.path.dirname(os.path.abspath(__file__))
print(app_dir)

# получить каталог на один уровень выше от скрипта
print(os.path.split(os.path.dirname(app_dir))[-1])
print(os.path.split(os.path.realpath(os.path.join(app_dir, "../../../../..")))[-1])
# получить каталог на два уровня выше от скрипта
print(os.path.split(os.path.realpath(os.path.join(app_dir, "../../../../../..")))[-1])
# получить каталог на три уровня выше от скрипта
print(os.path.split(os.path.realpath(os.path.join(app_dir, "../../../../../../..")))[-1])
