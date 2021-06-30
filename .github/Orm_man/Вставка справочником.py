r = conn.execute(ins, [
        {
            "first_name": "Vladimir", 
            "last_name": "Belousov", 
            "username": "Andescols", 
            "email":"andescols@mail.com", 
            "address": "Ul. Usmanova, bld. 70, appt. 223",
            "town": " Naberezhnye Chelny"
        },
        {
            "first_name": "Tatyana", 
            "last_name": "Khakimova", 
            "username": "Caltin1962", 
            "email":"caltin1962@mail.com",
            "address": "Rossiyskaya, bld. 153, appt. 509",
            "town": "Ufa"
        },
        {
            "first_name": "Pavel", 
            "last_name": "Arnautov", 
            "username": "Lablen", 
            "email":"lablen@mail.com",
            "address": "Krasnoyarskaya Ul., bld. 35, appt. 57",
            "town": "Irkutsk"
        },
    ])

print(r.rowcount)

