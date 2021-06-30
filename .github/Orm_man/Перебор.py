s = select([customers])
rs = conn.execute(s)
for row in rs:
    print(row)

