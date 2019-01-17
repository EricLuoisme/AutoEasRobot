import socket

obj = socket.socket()
obj.connect(("172.20.8.62", 8080))

while True:
    com = input("输入指令：")
    obj.sendall(bytes(com, encoding="utf-8"))
    if com == "结束":
        break
    rec = str(obj.recv(1024), encoding="utf-8")
    print("服务器返回："+rec)
obj.close()
