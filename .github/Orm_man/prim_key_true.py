from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey
metadata = MetaData()
parent = Table('parent', metadata,
    Column('acc_no', Integer(), primary=True),
    Column('acc_type', Integer(), nullable=False),
    Column('name', String(16), nullable=False),   
)
