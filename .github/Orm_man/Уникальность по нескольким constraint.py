parent = Table('parent', metadata,
    Column('acc_no', Integer, primary_key=True),
    Column('acc_type', Integer, nullable=False),
    Column('name', String(16), nullable=False),
    UniqueConstraint('acc_no', 'acc_type', name='uniq_1')
)