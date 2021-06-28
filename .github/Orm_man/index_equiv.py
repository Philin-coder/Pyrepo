a_table = Table('a_table', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False, index=True),
    Column('middle_name', String(100)),
    Column('last_name', String(100), nullable=False),    
)