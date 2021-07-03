s = select([items]).where(
    items.c.cost_price > 20
)

print(s)
r = conn.execute(s)
print(r.fetchall())

