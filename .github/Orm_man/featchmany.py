r = conn.execute(s)
print(r.fetchmany(2))
print(len(r.fetchmany(5)))  # вернется 4, потому что у нас всего 6 записей

