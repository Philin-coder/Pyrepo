from sqlalchemy import not_

select([items]).where(
    not_(items.c.cost_price.between(10, 20))
)

