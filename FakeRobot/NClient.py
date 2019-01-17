import socket

obj = socket.socket()
obj.connect(('127.0.0.100', 8080))
obj.listen(5)
conn, address = obj.accept()


def sent():
    global obj
    com = input("输入指令：")
    obj.sendall(bytes(com, encoding="utf-8"))


def receive():
    global obj
    return str(obj.recv(1024), encoding="utf-8")

# while True:
#     com = input("输入指令：")
#     obj.sendall(bytes(com, encoding="utf-8"))
#     if com == "结束":
#         break
#     rec = str(obj.recv(1024), encoding="utf-8")
#     print("服务器返回："+rec)
# obj.close()