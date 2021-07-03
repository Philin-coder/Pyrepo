select([customers]).where(
    customers.c.first_name.notin_(["Valeriy", "Vadim"])
)

