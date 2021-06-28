from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey

metadata = MetaData()

user = Table('users', metadata,
    Column('id', Integer(), primary_key=True),
    Column('user', String(200), nullable=False),
)

posts = Table('posts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(),  nullable=False),
    Column('user_id', ForeignKey("users.id")),
)

