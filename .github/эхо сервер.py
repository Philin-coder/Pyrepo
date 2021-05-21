import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    # Должен быть готов к чтению
    conn, addr = sock.accept()
    print('Создан сокет:', conn, 'для адреса:', addr)
    # включаем для него неблокирующий режим
    conn.setblocking(False)
    # регистрируем для прослушивания событий клиента
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    # Должен быть готов к чтению
    data = conn.recv(1000)
    if data:
        print('Отвечаем: ', repr(data), 'сокету =>', conn)
        conn.send(data)
    else:
        print('Закрытие соединения', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 8008))
sock.listen(5)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
