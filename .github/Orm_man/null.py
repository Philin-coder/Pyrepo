select([orders]).where(
    orders.c.date_shipped == None
)

