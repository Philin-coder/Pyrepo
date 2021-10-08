import sqlite3
import sys
import os
import binascii


def reader(fname, nm):
    with open(fname, 'rb') as fp:
        content = fp.read()
        # print(binascii.hexlify(content))
        fhex = (binascii.hexlify(content))
    fp.close()
    try:
        conn = sqlite3.connect(nm + '.' + 'db')
        cur = conn.cursor()
        cur.execute(
            '''create table if not exists music(id int auto_increment primary key not null, muzname varchar(50), mfile blob not null)''')

        cur.execute("insert into music(id,muzname,mfile)values(1,'my',?)", (fhex,))

        cur.execute("select  * from music ")
        results = cur.fetchall()
        print(results)
        conn.commit()
        with open(nm + '.' + 'sql', 'w') as fp:
            for line in conn.iterdump():
                fp.write("%s\n" % line)


    finally:
        cur.close()
        conn.close()

    # print(fhex)
    return fhex


if __name__ == '__main__':
    fhex = []
    nm = str(input("имя базы"))
    fname = '1.jpg'
    reader(fname, nm)
