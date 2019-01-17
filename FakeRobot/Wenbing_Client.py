import socket

sk = socket.socket()
sk.bind(("172.20.8.62", 8080))
sk.listen(5)

conn, address = sk.accept()
print("已监听到机器人连接，进入指令等待状态")

while True:
    rec = str(conn.recv(1024), encoding="utf-8")
    print("接收到的指令："+rec)
    conn.sendall(bytes("收到！", encoding="utf-8"))
