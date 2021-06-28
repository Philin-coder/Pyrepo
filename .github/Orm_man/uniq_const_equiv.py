parent = Table('parent', metadata,
    Column('id', Integer, primary_key=True),
    Column('ssn', Integer, unique=True, nullable=False),
    Column('name', String(16), nullable=False),    
)