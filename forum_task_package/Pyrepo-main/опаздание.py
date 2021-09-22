from datetime import datetime, timedelta

A1 = 5
A2 = 15


def late(now: str, deadline: str, bus: list) -> str:
    now = datetime.strptime(now, '%H:%M')
    deadline = datetime.strptime(deadline, '%H:%M')
    bus = [i for i in bus]

    delta = deadline - now - timedelta(minutes=A1 + A2)
    if delta.days < 0:
        return 'Опоздание'
    m = delta.seconds // 60
    ls = [m - i + A1 for i in bus if i >= A1]
    if not ls:
        return 'Опоздание'
    return 'Выйти через {} минут'.format(min(ls))


assert late('9:00', '10:00', [5, 15, 25]) == 'Выйти через 20 минут'
assert late('9:20', '9:35', [4, 25, 30]) == 'Опоздание'
print(late('12:00', '12:40', [0, 1, 4, 6, 25]))
