import socket

obj = socket.socket()
obj.connect(('127.0.0.100', 8080))
obj.listen(5)
conn, address = obj.accept()


def sent(message):
    global obj
    obj.sendall(bytes(message, encoding="utf-8"))


def receive():
    global obj
    return str(obj.recv(1024), encoding="utf-8")