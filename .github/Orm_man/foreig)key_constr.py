parent = Table('parent', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(16), nullable=False)
)

child = Table('child', metadata,
    Column('id', Integer, primary_key=True),
    Column('parent_id', Integer, nullable=False),
    Column('name', String(40), nullable=False),
    ForeignKeyConstraint(['parent_id'],['parent.id'])
)