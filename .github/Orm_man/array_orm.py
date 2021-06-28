from sqlalchemy import MetaData, Table, Column, Integer, ARRAY

metadata = MetaData()

employee = Table('employees', metadata,
    Column('id', Integer(), primary_key=True),
    Column('workday', ARRAY(Integer)),
)

