from sqlalchemy import MetaData, Table, Column, Integer, String, Text, ForeignKey

metadata = MetaData()

posts = Table('posts', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(),  nullable=False),    
)

tags = Table('tags', metadata,
    Column('id', Integer(), primary_key=True),
    Column('tag', String(200), nullable=False),
    Column('tag_slug', String(200),  nullable=False),    
)

post_tags = Table('post_tags', metadata,
    Column('post_id', ForeignKey('posts.id')),
    Column('tag_id', ForeignKey('tags.id'))
)

