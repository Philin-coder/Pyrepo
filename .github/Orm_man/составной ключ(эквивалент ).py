parent = Table('parent', metadata,
    Column('acc_no', Integer, nullable=False, primary_key=True),
    Column('acc_type', Integer, nullable=False, primary_key=True),
    Column('name', String(16), nullable=False),   
)