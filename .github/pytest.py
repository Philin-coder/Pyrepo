import csv
from operator import itemgetter

with open('studens.csv', encoding="utf-8", ) as file:
    reader = csv.reader(file, delimiter=';')
    students = list(reader)
    del students[0]

print(sorted(students, key=itemgetter(1)))
