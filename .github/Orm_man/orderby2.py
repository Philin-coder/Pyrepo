from sqlalchemy import asc

s = select([items]).where(
    items.c.quantity > 10
).order_by(asc(items.c.cost_price))

rs = conn.execute(s)
rs.fetchall()

