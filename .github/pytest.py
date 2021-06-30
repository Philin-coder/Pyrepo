from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, ForeignKey, CheckConstraint,Integer, String,Numeric,DateTime
from datetime import datetime
from sqlalchemy import engine

meta=MetaData()
engine=create_engine("postgresql+psycopg2://postgres:1@localhost/auto")

owner1=Table('owner1',meta,
Column('owner_id',Integer(),primary_key=True),
Column('owner_naim',String(200),nullable=False),
Column('owner_och',String(200),nullable=False),
Column('ownew_fam',String(200),nullable=False)
)
car=Table('car',meta,
Column('car_id',Integer(),primary_key=True),
Column('car_mark',String(200), nullable=False),
Column('car_model',String(200),nullable=False),
Column('owner_id',ForeignKey('owner1.owner_id'))
)
tofix=Table('tofix', meta,
Column('tofix_id',Integer(), primary_key=True),
Column('tofix_Isue',String(200), nullable=False),
Column('tofix_price',Numeric(10, 2),nullable=False),
Column('Car_id',ForeignKey('car.car_id')),
Column('tofix_date',DateTime(),default=datetime.now, onupdate=datetime.now),
CheckConstraint('tofix_price>0',name='Price_check')

)
meta.create_all(engine)
