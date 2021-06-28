employee = Table('employee', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(100), nullable=False),
    Column('salary', Integer(), nullable=False),
    CheckConstraint('salary < 100000', name='salary_check')
)