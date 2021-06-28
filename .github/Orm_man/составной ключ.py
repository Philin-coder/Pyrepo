from sqlalchemy import MetaData, Table, Column, Integer, ARRAY

metadata = MetaData()
parent = Table('parent', metadata,
    Column('acc_no', Integer, nullable=False),
    Column('acc_type', Integer, nullable=False),
    Column('name', String(16), nullable=False),
    PrimaryKeyConstraint('acc_no', 'acc_type', name='uniq_1')
)