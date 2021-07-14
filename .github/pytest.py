from openpyxl import load_workbook
w = load_workbook(filename='filename.xlsx', use_iterators=True)
sh = w.get_sheet_by_name('название_страницы'.decode('utf8'))