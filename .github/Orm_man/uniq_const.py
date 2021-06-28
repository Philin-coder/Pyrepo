parent = Table('parent', metadata,
    Column('id', Integer, primary_key=True),
    Column('ssn', Integer, nullable=False),
    Column('name', String(16), nullable=False),
    UniqueConstraint('ssn', name='unique_ssn')
)