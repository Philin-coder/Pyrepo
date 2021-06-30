from sqlalchemy import insert

conn = engine.connect()
ins = insert(customers)

r = conn.execute(ins, 
    first_name = "Vadim", 
    last_name = "Moiseenko", 
    username = "Antence73", 
    email = "antence73@mail.com",
    address = 'Partizanskiy Prospekt, bld. 28/А, appt. 51',
    town = ' Vladivostok'
)

