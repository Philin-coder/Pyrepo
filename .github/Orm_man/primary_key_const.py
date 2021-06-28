from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey
metadata = MetaData()
parent = Table('parent', metadata,
    Column('acc_no', Integer()),
    Column('acc_type', Integer(), nullable=False),
    Column('name', String(16), nullable=False),
    PrimaryKeyConstraint('acc_no', name='acc_no_pk')
)