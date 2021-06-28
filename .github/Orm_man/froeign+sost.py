parent = Table('parent', metadata,
    Column('id', Integer, nullable=False),
    Column('ssn', Integer, nullable=False),
    Column('name', String(16), nullable=False),    
    PrimaryKeyConstraint('id', 'ssn', name='uniq_1')
)

child = Table('child', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(40), nullable=False),
    Column('parent_id', Integer, nullable=False),
    Column('parent_ssn', Integer, nullable=False),
    ForeignKeyConstraint(['parent_id','parent_ssn'],['parent.id', 'parent.ssn'])
)