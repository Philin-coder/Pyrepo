select([items]).where(
    items.c.cost_price.between(10, 20)
)

