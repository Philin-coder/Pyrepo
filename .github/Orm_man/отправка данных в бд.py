ins = customers.insert().values(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
    username = 'Moseend',
    email = 'moseend@mail.com',
    address = 'Shemilovskiy 2-Y Per., bld. 8/10, appt. 23',
    town = ' Vladivostok'
)

conn = engine.connect()
r = conn.execute(ins)

