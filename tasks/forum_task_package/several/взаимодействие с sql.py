import pyodbc

conn = pyodbc.connect(driver='{SQL Server}', server='(local)', database='test', uid='', pwd='')
cursor = conn.cursor()
for row in cursor.execute("select * from stud"):
    print(row[0])
    print(row)
