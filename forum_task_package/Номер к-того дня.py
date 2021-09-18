import calendar
import datetime

now = calendar.Calendar()
K = 60  # номер дня в году
for y in range(2000, 2020):  # промежуток лет
    day = now.yeardayscalendar(year=y)[1][0][0][5]
    if day == 1:
        date = datetime.datetime(y, 1, 1) + datetime.timedelta(K)
        print(date.strftime('%d.%m.%Y'), date.weekday() + 1)

# 01.03.2000 3
# 02.03.2006 4
# 02.03.2017 4