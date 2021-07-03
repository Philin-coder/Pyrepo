s = select([items]).\
    where(
      (items.c.cost_price + items.c.selling_price > 50) & 
      (items.c.quantity > 10)
    )

