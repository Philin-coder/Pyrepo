from sqlalchemy import select

conn = engine.connect()

s = select([customers])
r = conn.execute(s)
print(r.fetchall())

