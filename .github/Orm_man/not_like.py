select([items]).where(
    not_(items.c.name.like("wa%"))
)

