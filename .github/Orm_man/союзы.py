from sqlalchemy import select, and_, or_, not_

select([items]).\
where(    
    and_(
        items.c.quantity >= 50,
        items.c.cost_price < 100,
    )
)

select([items]).\
where(    
    or_(
        items.c.quantity >= 50,
        items.c.cost_price < 100,
    )
)

select([items]).\
where(    
    and_(
        items.c.quantity >= 50,
        items.c.cost_price < 100,
        not_(
            items.c.name == 'Headphone'            
        ),        
    )
)

