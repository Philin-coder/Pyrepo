from sqlalchemy import insert

ins = insert(customers).values(
    first_name = 'Valeriy',
    last_name = 'Golyshkin',
    username = 'Fortioneaks',
    email = 'fortioneaks@gmail.com',
    address = 'Narovchatova, bld. 8, appt. 37',
    town = 'Magadan'
)
conn = engine.connect()
r = conn.execute(ins)
print(r.inserted_primary_key)

