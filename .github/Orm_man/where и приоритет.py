s = select([items]).\
    where(
      (items.c.cost_price > 200 ) | 
      (items.c.quantity < 5)
    ) 
print(s)

s = select([items]).\
    where(    
      ~(items.c.quantity == 50)
    ) 
print(s)

s = select([items]).\
    where(
      ~(items.c.quantity == 50) &
      (items.c.cost_price < 20)
    )
print(s)

