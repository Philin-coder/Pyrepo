import xlrd
import csv

data = xlrd.open_workbook('trial.xls')
sheet = data.sheet_by_index(0)
numbers = []
rows = sheet.nrows
for i in range(0, rows):
    numbers.append(sheet.row(i)[0])
print(type(numbers))
with open('list_to_csv.csv', 'w', newline='') as fp:
    csv_writer = csv.writer(fp)
    for item in numbers:
        csv_writer.writerow([item])
