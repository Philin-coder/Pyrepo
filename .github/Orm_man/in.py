select([customers]).where(
    customers.c.first_name.in_(["Valeriy", "Vadim"])
)

