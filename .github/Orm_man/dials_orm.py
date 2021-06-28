from sqlalchemy import MetaData, Table, Column, Integer
from sqlalchemy.dialects import postgresql

metadata = MetaData()

comments = Table('comments', metadata,
    Column('id', Integer(), primary_key=True),
    Column('ipaddress', postgresql.INET),
)

