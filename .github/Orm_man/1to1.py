from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey

metadata = MetaData()

employees = Table('employees', metadata,
    Column('employee_id', Integer(), primary_key=True),
    Column('first_name', String(200), nullable=False),
    Column('last_name', String(200), nullable=False),
    Column('dob', DateTime(), nullable=False),
    Column('designation', String(200), nullable=False),
)

employee_details = Table('employee_details', metadata,
    Column('employee_id', ForeignKey('employees.employee_id'), primary_key=True),
    Column('ssn', String(200), nullable=False),
    Column('salary', String(200), nullable=False),
    Column('blood_group', String(200), nullable=False),
    Column('residential_address', String(200), nullable=False),    
)

